from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Productos, Categorias

# Create your views here.

@login_required
def producto(request):
    context = {'titulo': 'Productos',
               'datos': Productos.objects.all(),}
    return render(request, 'productos.html',context)