from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.perfil_usuario, name='perfil_usuario'),
    path('profile/edit/', views.editar_perfil, name='editar_perfil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('politica-privacidad/', views.politica_de_privacidad, name='politica_privacidad'),
]