from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Perfil
from .forms import RegistroForm, EditarPerfilForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_usuario(request):
    perfil = Perfil.objects.get(user=request.user)
    niveles = ['Básico', 'Medio', 'Avanzado']
    puntos_requeridos = {
        'Básico': 10,
        'Medio': 100,
        'Avanzado': 1000,
    }
    nivel_actual = perfil.nivel
    experiencia_actual = perfil.experiencia
    experiencia_requerida = puntos_requeridos[nivel_actual]

    # Calcular la experiencia para el próximo nivel
    if nivel_actual != 'Avanzado':
        indice_nivel_actual = niveles.index(nivel_actual)
        proximo_nivel = niveles[indice_nivel_actual + 1]
        experiencia_proximo_nivel = puntos_requeridos[proximo_nivel]
        porcentaje_experiencia = (experiencia_actual / experiencia_requerida) 
        print(porcentaje_experiencia)
    else:
        experiencia_proximo_nivel = 'Max.'
        porcentaje_experiencia = 100

    return render(request, 'profile.html', {
        'perfil': perfil,
        'experiencia_actual': experiencia_actual,
        'experiencia_requerida': experiencia_requerida,
        'experiencia_proximo_nivel': experiencia_proximo_nivel,
        'porcentaje_experiencia': porcentaje_experiencia,
    })
    
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil_usuario')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

def politica_de_privacidad(request):
    return render(request, 'politica_privacidad.html')
