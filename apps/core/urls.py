from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name="home"),
    path('panel/', views.panel_view, name="panel"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('change_password/', views.change_password_view, name="change_password"),
    path('profile/<int:teacher_id>/', views.profile_view, name="profile"),
    path('public_profile/<int:teacher_id>/', views.public_profile, name="public_profile"),
    path('create_teacher/', views.create_teacher, name="create_teacher"),
]