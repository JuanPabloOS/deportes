from django.shortcuts import render
from django.http import HttpResponse
from apps.team.models import Team
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
# Create your views here.
def home_view(request):
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams':teams})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse("Binevenido")
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponse("Hasta luego")

def profile_view(request):
    return render(request, 'profile.html')

def changePassword_view(request):
    return render(request, 'changePassword.html')