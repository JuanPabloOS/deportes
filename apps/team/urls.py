from django.urls import path
from . import views
urlpatterns = [
    path('team_details/<int:id_equipo>/', views.team_details_view, name="team_details"),
    path('register/team/', views.register_team, name="register_team"),
    path('register/student/', views.register_student, name="register_student"),
]