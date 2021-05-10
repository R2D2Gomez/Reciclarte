from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

mi_nombre="Claudia"
mi_apellido="Gomez"
mi_temas=["plantillas","modelo","controlador"]

def una_plantilla(request): #primera vista
    # doc_externo=open("C:/python/reciclarte/reciclarte/plantillas/mi_plantilla.html")
    # plt=Template (doc_externo.read())
    # doc_externo.close()
    doc_externo=loader.get_template ('mi_plantilla.html')
    #ctx=Context({"mi_nombre_persona":mi_nombre, "mi_apellido_persona":mi_apellido, "mis_temas":mi_temas})
    #documento=plt.render(ctx)
    documento=doc_externo.render({"mi_nombre_persona":mi_nombre, "mi_apellido_persona":mi_apellido, "mis_temas":mi_temas})
    return HttpResponse (documento)

def querer(request):
    return HttpResponse ("te amo sofi")

def calculaedad(request, edad, agno):
    #edadactual=16
    periodo=agno-2021
    edadfutura=edad+periodo
    documento="<html><body><strong>tendras en el año %s tendras %s años </strong></body></html>" %(agno, edadfutura)
    return HttpResponse(documento)