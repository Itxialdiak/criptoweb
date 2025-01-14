from django.contrib import admin
from .models import HistoriaEp, TecnicaCriptografica, PeriodoHistoria

admin.site.register(PeriodoHistoria)
admin.site.register(HistoriaEp)
admin.site.register(TecnicaCriptografica)