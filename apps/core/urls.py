from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name="home"),
    path('profile/', views.profile_view, name="profile"),
    path('changePassword/', views.changePassword_view, name="changePassword")
]