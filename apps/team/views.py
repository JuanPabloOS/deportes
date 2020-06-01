from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# MODELOS
from .models import Team
from .models import Student
# Create your views here.
from .forms import StudentForm, TeamForm
def equipos(request):
    # Todos los equipos
    equipos = Team.objects.all()
    print("===========")
    print(equipos)
    print("===========")
    return HttpResponse(equipos)

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


def team_details(request, Team_id):
    """ Vista que registra un alumno en un taller """
    if request.method == 'POST':
        form = StudentForm(request.POST)        
        if form.is_valid():
            form.save()
            return redirect('team_details', Team_id)
        team = get_object_or_404(Team, pk=Team_id)
        students = Student.objects.filter(Team_id = Team_id)
        return render(request, 'team_details.html',{'form':form, 'students':students, 'team':team})

    team = get_object_or_404(Team, pk=Team_id)
    students = Student.objects.filter(Team_id = Team_id)
    form = StudentForm(initial={'Team':Team_id})
    return render(request, 'team_details.html',{'form':form, 'students':students, 'team':team})
    
def edit_team(request, Team_id):    
    # team = Team.objects.get(pk=Team_id)
    team = get_object_or_404(Team, pk=Team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, 'Listo!')
        else:
            messages.error(request, 'Faltan datos')
    form = TeamForm(instance=team)
    return render(request, 'edit_team.html', {'form':form})