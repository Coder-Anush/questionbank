from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from papers.views import signup, CustomLoginView
from django.contrib.auth.views import LogoutView  # ✅ Add this import
from django.contrib import admin
from django.urls import path, include
from main.views import welcome_page  # import the welcome view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_page, name='home'),  # set home to welcome page
    path('', include('main.urls')),       # keep all other app routes
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/view/')),  # 🔁 Redirect homepage to /view/
    path('', include('papers.urls')),

    # Authentication
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
