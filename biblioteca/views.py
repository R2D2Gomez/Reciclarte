from django.shortcuts import render
from django.http import HttpResponse
from biblioteca.models import rec_material

# Create your views here.
def busqueda_elementos(request):
    return render(request,"busqueda_elementos.html")

def buscar(request):
    
    if request.GET["elemento"]:
        #mensaje="Articulo buscado: %r" %request.GET["elemento"]
        producto=request.GET["elemento"]
        articulos=rec_material.objects.filter(mat_elemento__icontains=producto)
        return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        mensaje="por favor introduzca un elemento"
    
    return HttpResponse(mensaje)