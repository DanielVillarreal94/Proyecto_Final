from django.contrib import admin
from rol.models import Docente, Materia, Estudiante, Nota
# Register your models here.

admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Estudiante)
admin.site.register(Nota)