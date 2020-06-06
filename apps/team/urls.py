from django.urls import path
from . import views
urlpatterns = [
    path('team_details/<int:Team_id>/', views.team_details, name="team_details"),
    path('edit_team/<int:Team_id>/', views.edit_team, name="edit_team"),
    path('delete_student/<int:student_id>/', views.delete_student, name="delete_student"),
    path('liberar_student/<int:student_id>/', views.liberar_student, name="liberar_student"),
    path('create_team/', views.create_team, name="create_team"),
]