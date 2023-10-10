from .import views 

from django.urls import path, include

urlpatterns = [
    path('',views.home),
    path('registrarCurso/', views.registrarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    
]

