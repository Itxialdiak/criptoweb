from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from .models import Nivel, Actividad, Pregunta
from .forms import PruebaForm
from usuarios.models import Perfil, UsuarioActividad

def index(request):
    return render(request, 'index.html')

@login_required
def panel_actividades(request):
    niveles = Nivel.objects.all()
    actividades_por_nivel = {}
    user_nivel = request.user.perfil.nivel

    for nivel in niveles:
        if Nivel.objects.filter(nombre=user_nivel).exists():
            user_nivel_obj = Nivel.objects.get(nombre=user_nivel)
            # Comparar niveles para determinar acceso
            # Asumamos un orden: Básico < Medio < Avanzado
            orden = {
                'Básico': 1, 
                'Fácil': 2,
                'Medio': 3, 
                'Avanzado': 4,
                'Experto': 5,
                }
            if orden[user_nivel] >= orden[nivel.nombre]:
                actividades_por_nivel[nivel.nombre] = Actividad.objects.filter(nivel_requerido=nivel)
            else:
                actividades_por_nivel[nivel.nombre] = None  # Usuario no tiene acceso

    context = {
        'niveles': niveles,
        'actividades_por_nivel': actividades_por_nivel,
        'user_nivel': user_nivel,
    }
    return render(request, 'panel_actividades.html', context)

@login_required
def actividad_detalle(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id)
    user_nivel = request.user.perfil.nivel
    niveles = [
        'Básico', 
        'Fácil',
        'Medio', 
        'Avanzado',
        'Experto',
        ]
    orden = {nivel: idx for idx, nivel in enumerate(niveles, start=1)}

    if orden[user_nivel] >= orden[actividad.nivel_requerido.nombre]:
        # El usuario tiene acceso
        usuario_actividad, created = UsuarioActividad.objects.get_or_create(perfil=request.user.perfil, actividad=actividad)
        return render(request, 'actividad_detalle.html', {'actividad': actividad})
    else:
        # No tiene acceso
        return render(request, 'acceso_denegado.html', {'actividad': actividad})
    
@login_required
def realizar_prueba_nivel(request, nivel_nombre):
    nivel = get_object_or_404(Nivel, nombre=nivel_nombre)
    actividades = Actividad.objects.filter(nivel_requerido=nivel)
    if actividades.exists():
        actividad = random.choice(actividades)
        return redirect('actividad_detalle', actividad_id=actividad.id)
    else:
        messages.error(request, 'No hay actividades disponibles para este nivel.')
        return redirect('panel_actividades')

def verificar_respuesta(request, actividad_id):
    if request.method == 'POST':
        actividad = get_object_or_404(Actividad, id=actividad_id)
        respuesta_usuario = request.POST.get('respuesta')
        
        if respuesta_usuario.strip().lower() == actividad.solucion.strip().lower():
            # Respuesta correcta
            usuario_actividad, created = UsuarioActividad.objects.get_or_create(usuario=request.user, actividad=actividad)
            usuario_actividad.estado = True
            usuario_actividad.save()
            
            perfil = request.user.perfil
            perfil.experiencia += actividad.puntos
            perfil.save()
            
            # Verificar si el usuario sube de nivel
            verificar_nivel(perfil)
            
            messages.success(request, '¡Felicidades! Has resuelto correctamente la actividad.')
            return redirect('actividad_detalle', actividad_id=actividad_id)
        else:
            # Respuesta incorrecta
            messages.error(request, 'La respuesta es incorrecta. ¡Inténtalo de nuevo!')
            return redirect('actividad_detalle', actividad_id=actividad_id)

        
def verificar_nivel(perfil):
    niveles = [
        'Básico', 
        'Fácil',
        'Medio', 
        'Avanzado',
        'Experto',
    ]
    puntos_requeridos = {
        'Básico': 0,
        'Fácil': 100,
        'Medio': 1000,
        'Avanzado': 10000,
        'Experto': 100000,
    }
    
    for nivel in niveles:
        if perfil.experiencia >= puntos_requeridos[nivel]:
            perfil.nivel = nivel
    perfil.save()