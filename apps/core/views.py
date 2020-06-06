from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from apps.team.models import Team
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Profile
from .forms import ProfileForm
from .forms import TeacherForm
# Create your views here.


def home_view(request):
    """" Vista que muestra la oferta de talleres """
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})


@login_required
def panel_view(request):
    """ Vista que muestra el panel de control """
    teams = Team.objects.all()
    return render(request, 'panel.html', {'teams': teams})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Listo, contraseña actualizada')
        else:
            messages.error(request, 'Porfavor revisa tus datos')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def profile_view(request, teacher_id):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            'desc':'Aún no hay una descripción disponible',
        }
    )
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            if form.has_changed():
                new_profile = form.save(commit=False)
                new_profile.user_id = request.user.id
                new_profile.save()
                messages.success(request, 'Listo, perfil actualizado')
            else:
                messages.info(request, 'No has hecho cambios')
        else:
            messages.error(request, 'No se pudo actualizar tu perfil')
    form = ProfileForm(instance=profile)
        
    return render(request, 'profile.html', {'form':form, 'profile':profile})

def public_profile(request, teacher_id):
    profile = get_object_or_404(Profile, user_id=teacher_id)
    return render(request, 'public_profile.html', {'profile':profile})


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='panel')
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo registrar, revisa tus datos')
    form = TeacherForm()
    return render(request, 'create_teacher.html', {'form':form})