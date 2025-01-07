from django.urls import path
from . import views

urlpatterns = [
    path('historia/', views.historia_lista, name='historia_lista'),
    path('historia/<int:ep_id>/', views.historia_detalle, name='historia_detalle'),
    path('tecnicas/', views.tecnica_lista, name='tecnica_lista'),
]
