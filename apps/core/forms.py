from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)

class TeacherForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','last_name', 'first_name',)

        widgets = {
            'last_name': forms.TextInput(attrs={'required':True}),
            'first_name': forms.TextInput(attrs={'required':True}),
        }