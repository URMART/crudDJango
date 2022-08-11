from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarEstudiante/',views.registrarEstudiante),
    path('edicionEstudiante/<cedula>',views.edicionEstudiante),
    path('editarEstudiantes/',views.editarEstudiantes),
    path('eliminarEstudiante/<cedula>',views.eliminarEstudiante)
    


] 