from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')  # Redirige a la página de inicio
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})