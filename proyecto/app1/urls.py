from django.urls import path
from . import views

urlpatterns = [
    path('parroquias/', views.listar_parroquias, name='listar_parroquias'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear/parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear/barrio/', views.crear_barrio, name='crear_barrio'),
]
