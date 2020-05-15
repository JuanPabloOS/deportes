from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    ATLETISMO='Atletismo'
    BASKETBALL='Basketball'
    ESPORTS='eSports'
    FUTBOL='Futbol'
    HANDBALL='Handball'
    TENIS='Tenis'
    PINGPONG='Ping-Pong'
    TIROCONARCO='Tiro con arco'
    TOCHITO='Tochito'
    VOLEIBOL='Voleibol'
    SPORT_CHOICES=[
        (ATLETISMO,'Atletismo'),
        (BASKETBALL,'Basketball'),
        (ESPORTS,'ESports'),
        (FUTBOL,'Futbol'),
        (HANDBALL,'Handball'),
        (TENIS,'Tenis'),
        (PINGPONG,'Ping pong'),
        (TIROCONARCO,'Tiro con arco'),
        (TOCHITO,'Tochito'),
        (VOLEIBOL,'Voleibol'),
    ]
    CANCHA_PASTO = 'La cancha de pasto'
    CANCHA_TECHADA = 'La cancha techada'
    CAMPO_DE_TIRO = 'Campo de tiro'
    CAFETERIA = 'La cafe'
    PLACES_CHOICES = [
        (CANCHA_PASTO, 'La cancha de pasto'),
        (CANCHA_TECHADA, 'La cancha techada'),
        (CAMPO_DE_TIRO, 'Campo de tiro'),
        (CAFETERIA,'La cafe'),
    ]
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.CharField(max_length=25, choices=SPORT_CHOICES, default=FUTBOL)
    max_students = models.IntegerField(null=True, blank=True)
    schedule = models.CharField(max_length=50)
    place = models.CharField(max_length=25, choices=PLACES_CHOICES, default=CANCHA_PASTO)


class Student(models.Model):
    SOF18 = 'SOF18'
    LAT18 = 'LAT18'
    TEL18 = 'TEL18'
    INF18 = 'INF18'
    INC18 = 'INC18'
    PLAN_CHOICES = [
        (SOF18,'SOF18'),
        (LAT18,'LAT18'),
        (TEL18,'TEL18'),
        (INF18,'INF18'),
        (INC18,'INC18'),
    ]

    PRIMERO = 1
    SEGUNDO = 2
    TERCERO = 3
    SEMESTER_CHOICES=[
        (PRIMERO, 'Primero'),
        (SEGUNDO, 'Segundo'),
        (TERCERO, 'Tercero'),
    ]
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    expediente = models.IntegerField(unique=True)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    group = models.IntegerField()
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default=PRIMERO)
    plan = models.CharField(max_length=5, choices=PLAN_CHOICES, default='SOF18')
    liberado = models.BooleanField(default=False, blank=True)
    date_enrollment =  models.DateTimeField(auto_now_add=True, blank=True)