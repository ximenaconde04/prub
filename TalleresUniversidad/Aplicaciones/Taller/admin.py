from django.contrib import admin
from .models import Taller, Alumno, InscripcionTaller

# Register your models here.

admin.site.register(Taller)
admin.site.register(Alumno)
admin.site.register(InscripcionTaller)
