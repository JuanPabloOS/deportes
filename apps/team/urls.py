from django.urls import path
from . import views
urlpatterns = [
    path('equipos/', views.equipos, name="equipos"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('estudiantes/plan/<str:plan>/', views.estudiantes_plan, name="estudiantesByPlan"),
    path('estudiantes/equipo/<int:id_equipo>/', views.estudiantes_equipo, name="estudiantesByTeam"),
]