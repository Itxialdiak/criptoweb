from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import HistoriaEp, TecnicaCriptografica, PeriodoHistoria

def historia_lista(request):
    periodos = PeriodoHistoria.objects.all().order_by('orden')
    for periodo in periodos:
        periodo.episodios = periodo.historiaep_set.all().order_by('orden')
    return render(request, 'historia_lista.html', {'periodos': periodos})

def historia_detalle(request, episodio_id):
    episodio = get_object_or_404(HistoriaEp, id=episodio_id)
    return render(request, 'historia_detalle.html', {'episodio': episodio})

def tecnica_lista(request):
    tecnicas = TecnicaCriptografica.objects.all()
    query = request.GET.get('q')
    tipo = request.GET.get('tipo')
    if query:
        tecnicas = tecnicas.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    if tipo:
        tecnicas = tecnicas.filter(type=tipo)
    tipos = TecnicaCriptografica.objects.values_list('type', flat=True).distinct()
    return render(request, 'tecnica_lista.html', {'tecnicas': tecnicas, 'tipos': tipos})    