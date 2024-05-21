from django.urls import path
from . import views

urlpatterns = [
    path('', views.talleres),
    path('alumnos/', views.alumnos),
    path('inscripcionTaller/', views.inscripcionTaller), # Path para renderizar pantalla de inscripcion si taller pre seleccionado
    path('inscripcionTallerDirect/<tallerPk>', views.inscripcionTallerDirect), # Path para renderizar pantalla de inscripcion con taller pre seleccionado
    path('inscribirAlumno/', views.inscribirAlumno), # Path para accion de inscripcion
    path('generarDiploma/<inscripcionPk>', views.generarDiploma), # Path para generar diploma con datos de alumno
    path('eliminarInscripcion/<inscripcionPk>', views.eliminarInscripcion), # Path para eliminar alumno y registro de inscripcion
]