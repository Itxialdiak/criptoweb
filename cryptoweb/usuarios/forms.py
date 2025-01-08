from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Nota

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username", 
            "email", 
            "first_name", 
            "last_name", 
            "password1", 
            "password2"
            ]
        
class NotaForm(forms.ModelForm):
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tus notas aquí...'}),
        required=True
    )

    class Meta:
        model = Nota
        fields = ['contenido']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
