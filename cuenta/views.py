from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def perfil(request):
    context = {'titulo': 'Perfil'}
    return render(request, 'perfil.html',context)