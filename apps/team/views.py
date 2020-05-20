from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# MODELOS
from .models import Team
from .models import Student
# FORMULARIOS
from .forms import TeamForm
from .forms import StudentForm

def estudiantes(request):
    # Todos los estudiantes
    estudiantes = Student.objects.all()
    print("===========")
    print(estudiantes)
    print("===========")
    return HttpResponse(estudiantes)

def team_details_view(request, id_equipo):
    # tODOS LOS ESTUDIANTES QUE PERTENECEN A UN EQUIPO
    if request.method == 'POST':
        team = get_object_or_404(Team, pk=id_equipo)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('team_details', id_equipo)
    else:
        team = get_object_or_404(Team, pk=id_equipo)
        students = Student.objects.filter(Team_id = id_equipo)
        form = StudentForm(initial={'Team':team.id})
        return render(request, 'team_details.html', {'students':students, 'form':form, 'team':team })

def register_team(request):
    teams = Team.objects.all()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_team')
        return render(request, 'register_team.html', {'form' : form, 'teams':teams})
    form = TeamForm()
    return render(request, 'register_team.html', {'form' : form, 'teams':teams })

def register_student(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_student')
        return render(request, 'register_student.html', {'form': form, 'students': students})
    form = StudentForm()
    return render(request, 'register_student.html', {'form': form, 'students': students})
        