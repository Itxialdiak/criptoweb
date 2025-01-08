from django.urls import path
from . import views

urlpatterns = [
    # Define tus rutas aquí
    path('', views.index, name='index'),
    path('panel/', views.panel_actividades, name='panel_actividades'),
    path('actividad/<int:actividad_id>/', views.actividad_detalle, name='actividad_detalle'),
    path('actividad/<int:actividad_id>/verificar/', views.verificar_respuesta, name='verificar_respuesta'),
    path('prueba_nivel/<str:nivel_nombre>', views.realizar_prueba_nivel, name='prueba_nivel'),
]