from django import forms
from .models import Pregunta

class PruebaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        preguntas = kwargs.pop('preguntas')
        super(PruebaForm, self).__init__(*args, **kwargs)
        for pregunta in preguntas:
            self.fields[f'pregunta_{pregunta.id}'] = forms.ChoiceField(
                label=pregunta.texto,
                choices=[
                    (pregunta.opcion1, pregunta.opcion1),
                    (pregunta.opcion2, pregunta.opcion2),
                    (pregunta.opcion3, pregunta.opcion3),
                ],
                widget=forms.RadioSelect,
            )