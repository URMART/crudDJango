from django.shortcuts import redirect, render
from .models import EstudiantesAdsi
# Create your views here.

def home(request):

    estudiantes= EstudiantesAdsi.objects.all()

    return render(request,"gestionEstudiantes.html",{'estudiantes':estudiantes})


def registrarEstudiante(request):

    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    cedula=request.POST['txtCedula']
    edad=request.POST['edad']


    estudiante= EstudiantesAdsi.objects.create(nombre=nombre,apellido=apellido,cedula=cedula,edad=edad)

    return redirect("/")

    
def   edicionEstudiante(request,cedula):
    

    estudiante= EstudiantesAdsi.objects.get(cedula=cedula)

    return render(request, "edicionEstudiante.html",{'estudiante':estudiante})


def editarEstudiantes(request):

    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    cedula=request.POST['txtCedula']
    edad=request.POST['edad']

    estudiante= EstudiantesAdsi.objects.get(cedula=cedula)
    estudiante.nombre=nombre
    estudiante.apellido=apellido
    estudiante.cedula=cedula
    estudiante.edad=edad

    estudiante.save()

    return redirect('/')


def eliminarEstudiante(request,cedula): 

    estudiante= EstudiantesAdsi.objects.get(cedula=cedula)

    estudiante.delete()

    return redirect("/")




