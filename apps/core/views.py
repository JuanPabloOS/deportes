from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from apps.team.models import Team
# Create your views here.
def home_view(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams':teams})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST["username"], password = request.POST["password"])
        if user is not None:
            request.session.set_expiry(36000)
            login(request, user)
            return redirect('panel')
        return redirect('login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

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
    form = ProfileForm()
    return render(request, 'sign_up.html', {'form':form})