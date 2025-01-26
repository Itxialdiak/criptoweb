from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
        required=True,
        label='' 
    )

    class Meta:
        model = Nota
        fields = ['contenido']
        
    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.template = 'bootstrap5/table_inline_formset.html'
        self.helper.add_input(Submit('submit', 'Guardar Nota'))

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
