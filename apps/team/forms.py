from django import forms
from .models import Team
from .models import Student

class TeamForm(forms.ModelForm):
    
    class Meta:
        model = Team
        fields = '__all__'

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        exclude = ('liberado',)
        labels = {
            'Team':''
        }
        widgets={
            'Team':forms.NumberInput(attrs={'hidden':True})
        }

        

    
