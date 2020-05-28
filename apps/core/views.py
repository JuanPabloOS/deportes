from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from apps.team.models import Team
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
# Create your views here.
def home_view(request):
    """" Vista que muestra la oferta de talleres """
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams':teams})

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

def changePassword_view(request):
    return render(request, 'changePassword.html')