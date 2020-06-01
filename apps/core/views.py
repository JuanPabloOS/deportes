from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from apps.team.models import Team
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import ProfileForm
from .forms import TeacherForm
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.
def home_view(request):
    """" Vista que muestra la oferta de talleres """
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams':teams})

def view_profile(request, teacher_id):
    """" Vista que muestra el perfil de un profesor """
    try:
        profile = Profile.objects.get(user_id=teacher_id)
        return render(request, 'view_profile.html', {'profile':profile})
    except :
        return render(request, 'view_profile.html', {'profile':None})


def panel_view(request):
    """ Vista que muestra el panel de control """
    teams = Team.objects.all()
    return render(request, 'panel.html', {'teams':teams})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, 'login.html', {'form':AuthenticationForm()})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("login")

def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def panel_view(request):
    teams = Team.objects.all()
    return render(request, 'panel.html', {'teams':teams})

@login_required
def changePassword_view(request):
    return render(request, 'changePassword.html')


@login_required
def profile_view(request):
    try:
        # Intentar buscar un perfil existente para el usuario
        profile = Profile.objects.get(user_id=request.user.id)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                if form.has_changed():
                    new_profile = form.save(commit=False)
                    new_profile.user = request.user
                    new_profile.save()
                    messages.success(request, 'Perfil actualizado')
                return render(request, 'profile.html', {'form':form})
        form = ProfileForm(instance=profile)
        return render(request, 'profile.html', {'form':form})
    except Profile.DoesNotExist: 
        # Al no encontrar un perfil entonces deberá crearlo   
        form = ProfileForm()
        messages.info(request, 'Aún no has completado tu perfil')
        return render(request, 'complete_profile.html', {'form':form})




@require_POST
@login_required
def complete_profile(request):
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        print("IT IS CORRECT =========")
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        messages.success(request, 'Tu perfil se ha actualizado')
        return redirect('profile')
    else:
        return render(request, 'profile.html', {'form':form})

@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Listo')
        return render(request, 'update_password.html', {'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'update_password.html', {'form':form})



@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='panel')
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
            return redirect('create_teacher')
        return render(request, 'register_team.html', {'form':form})
    else:
        form = TeacherForm()
        return render(request, 'register_team.html', {'form':form})