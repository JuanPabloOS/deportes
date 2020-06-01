from django import forms
from .models import Student, Team

class StudentForm(forms.ModelForm):
    """ Formulario para registrar un alumno """

    class Meta:
        model = Student
        exclude = ('liberado',)
        labels = {
            'Team':''
        }
        widgets = {
            'Team' : forms.NumberInput(attrs={'hidden':True})
        }

class TeamForm(forms.ModelForm):
    """ Formulario para registrar un alumno """

    class Meta:
        model = Team
        fields = '__all__'
        
