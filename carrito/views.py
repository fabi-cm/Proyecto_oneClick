from django.shortcuts import render

# Create your views here.
def carrito(request):
    context = { 'titulo': 'Carrito',}
    return render(request, 'carrito.html', context)


