from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
# MODELOS
from .models import Team
from .models import Student
# Create your views here.
from .forms import StudentForm, TeamForm

def team_details(request, Team_id):
    # tODOS LOS ESTUDIANTES QUE PERTENECEN A UN EQUIPO
    if request.method == 'POST':
        team = get_object_or_404(Team, pk=Team_id)
        form = StudentForm(request.POST)
        if form.is_valid():    
            # Verificar que aún hay espacio
            enrrolment_students = Student.objects.filter(Team_id=Team_id).count()
            print(enrrolment_students)
            print(team.max_students)
            if team.max_students >= enrrolment_students:
                # form.save()
                messages.success(request, 'Listo')
            else:
                messages.error(request, 'Cupo lleno')
        return redirect('team_details', Team_id)
    else:
        team = get_object_or_404(Team, pk=Team_id)
        students = Student.objects.filter(Team_id = Team_id)
        form = StudentForm(initial={'Team':team.id})
        return render(request, 'team_details.html', {'students':students, 'form':form, 'team':team })



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

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='panel')
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
            return redirect('create_team')
        return render(request, 'register_team.html', {'form':form})
    else:
        form = TeamForm()
        return render(request, 'register_team.html', {'form':form})
