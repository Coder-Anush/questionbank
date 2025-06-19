from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import FileResponse
from django import forms
from .models import QuestionPaper
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

def welcome_page(request):
    return render(request, 'welcome.html')


# ---------- Welcome & Info Pages ----------
def welcome(request):
    return render(request, 'welcome.html')

def become_uploader(request):
    return render(request, 'become_uploader.html')

def admin_info(request):
    return render(request, 'admin_info.html')

# ---------- Upload ----------
@login_required
def upload_paper(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.uploader = request.user
            paper.save()
            return redirect('upload_success')
    else:
        form = QuestionPaperForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def upload_success(request):
    return render(request, 'upload_success.html')

# ---------- View Papers ----------
@login_required
def view_papers(request):
    papers = QuestionPaper.objects.filter(is_approved=True)

    query = request.GET.get('q')
    year = request.GET.get('year')
    slot = request.GET.get('slot')
    faculty = request.GET.get('faculty')

    if query:
        papers = papers.filter(Q(course_name__icontains=query) | Q(course_code__icontains=query))
    if year:
        papers = papers.filter(year__icontains=year)
    if slot:
        papers = papers.filter(slot__icontains=slot)
    if faculty:
        papers = papers.filter(faculty__icontains=faculty)

    return render(request, 'view_paper.html', {'papers': papers})

@login_required
def download_paper(request, paper_id):
    paper = QuestionPaper.objects.get(id=paper_id)
    return FileResponse(paper.file.open(), as_attachment=True, filename=f"{paper.course_name}.pdf")

# ---------- My Uploads ----------
@login_required
def my_uploads(request):
    papers = QuestionPaper.objects.filter(uploader=request.user).order_by('-uploaded_at')
    return render(request, 'my_uploads.html', {'papers': papers})

# ---------- Manage Users ----------
@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    UserModel = User
    query = request.GET.get('q')
    users = UserModel.objects.filter(is_superuser=False)

    if query:
        users = users.filter(Q(username__icontains=query) | Q(first_name__icontains=query))

    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    users_page = paginator.get_page(page)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        User.objects.filter(id=user_id, is_superuser=False).delete()
        return redirect('manage_users')

    return render(request, 'manage_users.html', {'users': users_page, 'query': query})
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms

# ---------- Signup ----------
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Name')
    username = forms.CharField(label='Registration Number')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_papers')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# ---------- Login ----------
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
