from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Team
from .models import Student
# Create your views here.
from .forms import StudentForm, TeamForm


@login_required
def team_details(request, Team_id):
    """ Vista que registra un alumno en un taller """
    team = get_object_or_404(Team, pk=Team_id)
    students = Student.objects.filter(Team_id = Team_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)   
        total_students = Student.objects.filter(Team_id=Team_id).count()
        if total_students < team.max_students: 
            if form.is_valid():
                form.save()
                messages.success(request, 'Listo')
                return redirect('team_details', Team_id)
            return render(request, 'team_details.html',{'form':form, 'students':students, 'team':team})
        else:
            messages.error(request, 'Cupo lleno')
            return render(request, 'team_details.html',{'form':form, 'students':students, 'team':team})
    form = StudentForm(initial={'Team':Team_id})
    return render(request, 'team_details.html',{'form':form, 'students':students, 'team':team})

@login_required  
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
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    team_id = student.Team.id
    student.delete()
    return redirect('team_details', team_id)

@login_required
def liberar_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.liberado = True
    team_id = student.Team.id
    student.save()
    return redirect('team_details', team_id)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='panel')
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo registrar, revisa tus datos')
    form = TeamForm()
    return render(request, 'create_team.html', {'form':form})