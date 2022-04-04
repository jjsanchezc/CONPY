# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from django.shortcuts import render
from fileinput import filename
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import apps.home.dataManagement.ingresos.manage as idm
import apps.home.dataManagement.gastos.manage as gdm
from core import settings


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def upload(request):
    print("llega hasta aca")
    if request.method=="POST":
        uploaded_file=request.FILES['documento']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request,'upload-download.html')




@login_required(login_url="/login/")
def read_new_input(request):
    """metodo para leer el input de ingresos, este llama a las 
    funciones manage.py para poder procesarlos

    Returns:
        django.http.response.HttpResponse: devuelve a la pagina
         de ingresos
    """
    descr=request.POST.get('descripcion')
    cant=request.POST.get('cantidad')
    msg=None
    exito=None
    if request.POST.get('tipo')=='ingreso':
        
        org=request.POST.get('origen/destino')

        if cant!="" and org!="" :
            try:
                idm.add_ingresos(str(org),str(descr),float(cant))
                exito="se ha añadido con exito a la base de datos"
            except ValueError:
                msg="no se han introducido datos correctos en cantidad"
        else:
            msg="Has dejado espacios obligatorios vacios"
    elif request.POST.get('tipo')=='gasto':
        destino=request.POST.get('origen/destino')

        if cant!="" and destino!="" :
            try:
                gdm.add_gastos(str(destino),str(descr),float(cant))
                exito="se ha añadido con exito a la base de datos"
            except ValueError:
                msg="no se han introducido datos correctos en cantidad"
        else:
            msg="Has dejado espacios obligatorios vacios"
        print("gastos")
    else:
        print("no entré")


    return render(request,'home/ingreso.html',{"msg":msg,"exito":exito})


def a(request):
    print("--------------------------------------------\nhola soy a")
