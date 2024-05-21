from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import *
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage

from io import BytesIO
import locale
from datetime import datetime
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape

# Create your views here.

def talleres(request):
    talleres = Taller.objects.all()
    return render(request, "tabs/talleres.html", {"talleres": talleres, "nbar": "talleres"})

def alumnos(request):
    alumnos = InscripcionTaller.objects.all()
    return render(request, "tabs/alumnos.html", {"alumnos": alumnos, "nbar": "alumnos"})

def inscripcionTaller(request):
    # Talleres para seleccion
    talleres = Taller.objects.all()

    # Alumnos para seleccion
    alumnos = Alumno.objects.all()

    return render(request, "forms/inscripcion.html", {"alumnos": alumnos, "talleres": talleres, "nbar": "inscripcion"})

def inscripcionTallerDirect(request, tallerPk):
    print("Iniciando inscripcion a taller con ID [{0}]".format(tallerPk))

    # Variable para taller seccionado
    taller = Taller.objects.get(pk = tallerPk)
    
    # Talleres para seleccion
    talleres = Taller.objects.all()

    # Alumnos para seleccion
    alumnos = Alumno.objects.all()

    return render(request, "forms/inscripcion.html", {
        "seleccionTaller": taller,
        "talleres": talleres,
        "alumnos": alumnos,
        "nbar": "inscripcion"
        })

def inscribirAlumno(request):
    # Obtiene informacion de taller
    taller = Taller.objects.get(pk = request.POST["idTaller"])

    isNewAlumno = request.POST.get("isNewAlumno", "")
    print("----->" + isNewAlumno)

    # Inicializa alumno vacio
    alumno = Alumno.objects.none

    # Crea alumno nuevo o usa existente
    if (request.POST.get("isNewAlumno", "") != "selected"):
        alumno = Alumno.objects.get(pk = request.POST["idAlumno"])
    else:
        alumno = Alumno.objects.create(
            numeroControl = request.POST["numeroControl"], nombreCompleto = request.POST["nombreCompleto"]
        )
    
    # Crea registro de inscripcion de alumno a taller
    InscripcionTaller.objects.create(
        taller = taller,
        alumno = alumno
    )

    return redirect('/alumnos')

def generarDiploma(request, inscripcionPk):
    # Obtiene datos a utilizar
    inscripcion = InscripcionTaller.objects.get(pk = inscripcionPk)
    
    # Establece idioma para formato de fecha
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    # Coloca datos para PDF en hoja en blanco
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=landscape(letter))

    p.drawString(350, 290, inscripcion.alumno.nombreCompleto)
    p.drawString(120, 210, inscripcion.taller.nombre)
    p.drawString(470, 210, "Instituto Tecnológico de Apizaco")
    p.drawString(180, 140, datetime.now().strftime("%d de %B de %Y"))

    p.showPage()
    p.save()
 
    buffer.seek(0)

    # Crea nuevo PDF con Reportlab
    nuevoPdf = PdfReader(buffer)
    
    # Lee template de archivo PDF
    pdfExistente = PdfReader(staticfiles_storage.open('diploma-template.pdf'), "rb")
    output = PdfWriter()
    
    # Une las pagina de PDF existente con la que tiene los datos
    page = pdfExistente.pages[0]
    page.merge_page(nuevoPdf.pages[0])
    output.add_page(page)

    # Escribe datos en buffer para descargar en browser
    finalBuffer = BytesIO()
    output.write(finalBuffer)

    finalBuffer.seek(0)

    # Utiliza file response para que el browser muestre opcion de guadar archivo
    return FileResponse(finalBuffer, as_attachment=True, filename=str(inscripcion.alumno.numeroControl) + "-diploma.pdf")


def eliminarInscripcion(request, inscripcionPk):
    inscripcion = InscripcionTaller.objects.get(pk = inscripcionPk)
    inscripcion.delete()
    
    messages.success(request, 'Registro eliminado correctamente!')

    return redirect('/alumnos')
