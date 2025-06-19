from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('upload/', views.upload_paper, name='upload'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('view/', views.view_papers, name='view_papers'),
    path('download/<int:paper_id>/', views.download_paper, name='download_paper'),
    path('myuploads/', views.my_uploads, name='my_uploads'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('become-uploader/', views.become_uploader, name='become_uploader'),
    path('admin-info/', views.admin_info, name='admin_info'),

    # Login/Signup
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
