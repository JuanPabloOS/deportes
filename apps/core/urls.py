from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name="home"),
    path('panel/', views.panel_view, name="panel"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('changePassword/', views.changePassword_view, name="changePassword"),
    path('profile/', views.profile_view, name="profile"),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('profile/', views.profile_view, name='profile'),
    path('update_password/', views.update_password, name='update_password'),
    path('view_profile/<int:teacher_id>/', views.view_profile, name='view_profile'),
    path('create_teacher/', views.create_teacher, name="create_teacher"),
]