from inscriptions.models import Inscrit,InscritAdmin,InscritPerfAdmin,InscritPerf
from django.contrib import admin

admin.site.register(Inscrit,InscritAdmin)
admin.site.register(InscritPerf,InscritPerfAdmin)
