from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import HistoriaEp, TecnicaCriptografica

def historia_lista(request):
    episodios = HistoriaEp.objects.order_by('orden')
    return render(request, 'historia_lista.html', {'episodios': episodios})

def historia_detalle(request, ep_id):
    episodio = get_object_or_404(HistoriaEp, id=ep_id)
    return render(request, 'historia_detalle.html', {'episodio': episodio})

def tecnica_lista(request):
    tecnicas = TecnicaCriptografica.objects.all()
    query = request.GET.get('q')
    if query:
        tecnicas = tecnicas.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    return render(request, 'tecnica_lista.html', {'tecnicas': tecnicas})
