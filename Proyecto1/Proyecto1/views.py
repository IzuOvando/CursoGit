from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self,nombre,apellido):

        self.nombre=nombre

        self.apellido=apellido

def saludo(request): # primera vista

    p1=Persona("Arturo","Diaz")

    #nombre="Juan"

    #apellido="Ovando"

    temas_curso=["plantillas","modelos","formularios","views","despliegue"]

    fecha=datetime.datetime.now()

    doc_externo=open("C:/Users/tyrae/Desktop/Curso Django/Proyecto1/Proyecto1/Plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora":fecha, "temas":temas_curso})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    html_despedida=open("C:/Users/tyrae/Desktop/Curso Django/Proyecto1/Proyecto1/Plantillas/despedida.html")

    plt=Template(html_despedida.read())

    html_despedida.close()

    con=Context()

    doc=plt.render(con)

    return HttpResponse(doc)

def damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""
    <html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </html>
    </body>
    </h1>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, agno, edad):

    periodo=agno-2020
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años"%(agno,edadFutura)

    return HttpResponse(documento)
