from django.shortcuts import render, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm

# Vista para listar parroquias y sus barrios
def listar_parroquias(request):
    parroquias = Parroquia.objects.prefetch_related('barrios')
    return render(request, 'parroquia_lista.html', {'parroquias': parroquias})

# Vista para listar barrios
def listar_barrios(request):
    barrios = Barrio.objects.select_related('parroquia')
    return render(request, 'barrio_lista.html', {'barrios': barrios})

# Vista para crear parroquia
def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquias')
    else:
        form = ParroquiaForm()
    return render(request, 'parroquia_form.html', {'form': form})

# Vista para crear barrio
def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm()
    return render(request, 'barrio_form.html', {'form': form})
