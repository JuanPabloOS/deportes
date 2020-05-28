from django import forms
from .models import Student

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