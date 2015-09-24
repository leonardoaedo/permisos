#!/usr/bin/python
# -*- encoding: utf-8 -*-
from dateutil.parser import *
from dateutil.tz import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from models import * 
from array import *
from numpy import *
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from edt.models import *
from django.views.generic import ListView
from django.views.generic.dates import WeekArchiveView
from django.shortcuts import get_object_or_404,render_to_response
from django.forms import ModelForm
from django import forms
from calendar import month_name
from django.core.context_processors import csrf
from django.db.models import Count
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from icalendar import Calendar, Event
from pytz import timezone
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from datetime import date, datetime, timedelta
from django.core import serializers
from funciones.session import estaLogeado
from datetime import datetime
from dateutil import tz
import time
import calendar
import icalendar
import pytz
import os
import json
import urllib
import time


#from icalendar import UTC # timezone
# Create your views here.
def login(request):
        if request.session.get('usuario',False):
                return redirect('/')#puse esa url para probar nomas
        else:
                if request.POST.get('username') and request.POST.get('password'):
                        usuario = request.POST.get('username')
                        password = request.POST.get('password')
                        try:
                                usuarioObj = Usuario.objects.get(username=usuario,password=password)
                                request.session['usuario'] = usuarioObj.id
                                return redirect('/')
                        except Exception as e:
                                return HttpResponseRedirect("/login/","El usuario o la contraseña son incorrectos!!!")


                else:
                        return render(request,'edt/login.html',{})

def logout(request):
            if not estaLogeado(request):
                return redirect("/login")

            try:
                    del request.session['usuario']
            except KeyError:
                    pass

            return redirect("/login")

def wsCalendario(request): # Web service que  genera calendario para cargar en pantalla 
        if not estaLogeado(request):
                return redirect("/login")
        usuarioObj = Usuario.objects.get(id=request.session['usuario'])

        usuario_id=request.session['usuario']
        #lista de los ids de los eventos ya ocupados
        ids = []
        for lista_ids in Eventos_en_Permisos.objects.all():
            ids.append(int(lista_ids.numero_evento.id))

         #data = serializers.serialize("json", Calendari.objects.filter(usuario_id=usuario_id))
         #Objeto.objects.all().exclude(id__in=lista) parta excluir los que estan en la lista
        lista = []
        for evento in Evento.objects.filter(usuario_id=usuario_id):
                evento.flageado = evento.id in ids                   
                #formateo de timezone a milisegundos
                from_zone = tz.gettz('UTC')
                to_zone = tz.gettz('America/Boise') 
                start = datetime.timetuple(evento.start)
                start = time.strftime('%Y-%m-%dT%H:%M:%SZ', start)
                start = datetime.strptime(start, '%Y-%m-%dT%H:%M:%SZ')
                start = start.replace(tzinfo=from_zone)
                start = start.astimezone(to_zone)
                start = 1000*(time.mktime(start.timetuple()))
                end = datetime.timetuple(evento.end)
                end = time.strftime('%Y-%m-%dT%H:%M:%SZ', end)
                end = datetime.strptime(end, '%Y-%m-%dT%H:%M:%SZ')
                end = end.replace(tzinfo=from_zone)
                end = end.astimezone(to_zone)
                end = 1000 * (time.mktime(end.timetuple()))
                #generacion de lista de eventos en formato json               

                lista.append({"used": evento.flageado,"id":evento.id, "start":start, "end":end, "title":usuarioObj.nombre+" "+usuarioObj.apellido1 ,"body":" ", "multi":0 ,"allDay":False, "extension_id":2})
                data = json.dumps(lista)
            
                    
        #retorna la info en formato JSON
        return HttpResponse(data, content_type = "application/json")
        #return HttpResponse(json.dumps(ids)) ==> verificacion de permisos ya ocupados

def comprobante(request, pk):
        if not estaLogeado(request):
            return redirect("/login")
        usuarioObj = Usuario.objects.get(id=request.session['usuario'])
            
        #idpermiso = Permiso.objects.get(id=int(pk))        
        permiso = Permiso.objects.get(id=pk)
        #evento = Eventos_en_Permisos.objects.filter(numero_permiso=idpermiso)
	
	
 
        return render_to_response("edt/comprobante.html",{ "permiso" : permiso,"usuario" : usuarioObj})
        #return HttpResponse({ "permiso" : permiso,"usuario" : usuarioObj,"evento" : evento})     

class PermisoFormSet(forms.ModelForm):
    class Meta:
       model = Permiso
       exclude = ["entrada","usuario","horas_solicitadas"]
    
class ResolucionFormSet(forms.ModelForm):
        class Meta:
           model = Resolucion
           exclude = [""]

        
@csrf_exempt
def urlcalendario(request):
    if not estaLogeado(request):
                return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    usuario_id=request.session['usuario']

    if request.method == 'POST':
        arrayDeEventos = json.loads(request.POST['data-calendario'])  #cargo los id de los eventos seleccionados
        reemplazante = request.POST.get('reemplazante')
        devuelve_horas = request.POST.get('devuelve_horas')
        documento_adjunto = request.POST.get('documento_adjunto')
                                                                      #en el calendario en formato json a una lista           
        eventos = Evento.objects.filter(id__in=arrayDeEventos) #consulto los eventos en la tabla Eventos segun los Id de la lista

        

    formset = PermisoFormSet(request.POST, request.FILES) 
   
    if formset.is_valid():
        permiso= formset.save(commit=False)
        
        permiso.usuario = usuarioObj
        permiso.relevante = reemplazante
        devuelve_horas = devuelve_horas
        documenot_adjunto = documento_adjunto
        permiso.save() # guardo los datos de Permiso en la BD

        if len(Permiso.objects.all()) == 0: # verifico si la tabla permisos esta vacia
            ultimopermiso = 1 # si esta vacia le asigno el valor 1
        else:
            #consulto el ultimo registro de la tabla Permiso
            ultimopermiso = Permiso.objects.all().order_by("-id")[0]

        suma = 0
        i = 0
        deltas = []        
        for evento in eventos:
            delta = evento.end - evento.start # calculo de la cantidad de horas solicitadas en segundos
            suma += delta.seconds / 55 / 55 / 0.75 #se divide por 55 por que los bloques son de 55 minutos, y equivalen a 1 hora // formula aplicable a las horas frente a alumnos
            deltag = delta.seconds / 55 / 55 / 0.75
            deltas.append(round(deltag,2))           
            suma = round(suma,2) # redondeo a 2 decimales
            evento_en_permiso = Eventos_en_Permisos(numero_evento=evento,numero_permiso=ultimopermiso,delta=deltas[i])
            i += 1
            evento_en_permiso.save()
            permiso.horas_solicitadas = suma
            permiso.save() # guardo suma aca despues de hacer el calculo
        

        #email a funcionario
        template = loader.get_template('edt/email_solicitud.html')
        context = RequestContext(request, {'nombre' : usuarioObj.nombre,'apellido' : usuarioObj.apellido1,'horas':permiso.horas_solicitadas,'numero':permiso.id})
        html = template.render(context)
        msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [usuarioObj.correo])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        #email a jefatura
        template = loader.get_template('edt/email_jefatura.html')
        context = RequestContext(request, {'jefe' : usuarioObj.jefatura.nombre,'horas':permiso.horas_solicitadas,'numero':permiso.id,'nombre' : usuarioObj.nombre,'apellido' : usuarioObj.apellido1,'rut': usuarioObj.rut,'dv':usuarioObj.dv,'nom_reemplazante':permiso.reemplazante.nombre,'ap_reemplazante':permiso.reemplazante.apellido1,'fecha': permiso.fecha_creacion})
        html = template.render(context)
        msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [usuarioObj.jefatura.correo1])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        
        return redirect("/comprobante/%d"%(ultimopermiso.id))
    # data = json.dumps({"suma" : suma,"ultimo" : ultimopermiso,"largo":len(eventos),"usuario":usuario_id,"reemplazante" : reemplazante,"devuelve_horas":devuelve_horas})
    # return HttpResponse(data, content_type = "application/json")
    else:
        formset = PermisoFormSet()
    return render_to_response("edt/main.html", {
        "form": formset,
    },context_instance=RequestContext(request)) 


class DocumentFormSet(forms.ModelForm):
        class Meta:
           model = Document
           exclude = [""]


def index(request):
        if not estaLogeado(request):
                return redirect("/login")
        usuarioObj = Usuario.objects.get(id=request.session['usuario'])
	
        if  usuarioObj.rol.id == 1:

            if request.method == 'POST':
                formset = DocumentFormSet(request.POST, request.FILES)
                if formset.is_valid():
                        document= formset.save(commit=False)
                        document.save()
                return redirect('/upload/%d'%(document.id))
            else:
                
                  formset = DocumentFormSet()
                  return render_to_response("edt/index.html", {"form": formset,"usuario": usuarioObj,},context_instance=RequestContext(request))
        else:
                return redirect("/main") 

def permisolst(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])     

    if  usuarioObj.rol.id != 2:
        #permiso =  Permiso.objects.all().order_by("-fecha_creacion")
        #IMPORTANTE: el codigo siguiente crea un campo virtual y luego cuenta cuantas resolciones tiene asociadas y si el contador es mayor a cero no lo toma en cuenta 
        permiso = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b=0).order_by("-fecha_creacion")

        paginator = Paginator(permiso,10) 
        
        try: pagina = int(request.GET.get("page",'1'))
        except ValueError: pagina = 1
            
        try:
            permiso = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            permiso = paginator.page(paginator.num_pages)   
            
        return render_to_response("edt/permisolst.html",{"permiso": permiso,"usuario" : usuarioObj,"permisoObj_list" : permiso.object_list,"months" : mkmonth_lst()})

    else:
        #if     usuarioObj.username == request.session['usuario']:
        if  usuarioObj.rol.id == 2:
            permiso = Permiso.objects.annotate(num_b=Count('resolucion')).filter(usuario=usuarioObj.id).order_by("-fecha_creacion")
            

            paginator = Paginator(permiso,10)       
            try: pagina = int(request.GET.get("page",'1'))
            except ValueError: pagina = 1       
            try:
                permiso = paginator.page(pagina)
            except (InvalidPage, EmptyPage):
                permiso = paginator.page(paginator.num_pages)


            
        return render_to_response("edt/permisolst.html",{"permiso": permiso,"usuario" : usuarioObj,"permisoObj_list" : permiso.object_list,"months" : mkmonth_lst()})


def upload(request, pk):
        if not estaLogeado(request):
            return redirect("/login")
        usuarioObj = Usuario.objects.get(id=request.session['usuario'])

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        iddocument = Document.objects.get(pk=int(pk))
        nombre = Document.objects.get(id=pk)
        
       	nombre_archivo = nombre.docfile.name
        folder = os.path.join(BASE_DIR, 'media/')
        contador = 0
        g = open(folder + nombre_archivo,'rb')
        gcal = Calendar.from_ical(g.read())
       
       
        for component in gcal.walk():         
            if component.name == "VEVENT":
                
                user = Document.objects.get(id=int(pk)).usuario.id
                nombre_funcionario = Document.objects.get(id=int(pk)).usuario.nombre
                apellido_funcionario = Document.objects.get(id=int(pk)).usuario.apellido1
                contador = contador + 1               
                CATEGORIES = component.get('CATEGORIES')
                #DTSTAMP = component.get('DTSTAMP').dt hora de creacion del archivo ics , no es relevante
                DTSTART = component.get('DTSTART').dt
                DTEND = component.get('DTEND').dt
                SUMMARY = component.get('SUMMARY')
                LOCATION = component.get('LOCATION')
                DESCRIPTION = component.get('DESCRIPTION')

                c = Evento(usuario_id=user,start=DTSTART,end=DTEND)               
                c.save()  
               
        g.close()
        return render_to_response("edt/upload.html",{ "apellido_funcionario": apellido_funcionario,"nombre_funcionario":nombre_funcionario,"user" : user , "DESCRIPTION" : DESCRIPTION, "LOCATION" : LOCATION, "contador" : contador, "DTEND" : DTEND,"DTSTART": DTSTART, "CATEGORIES" : CATEGORIES,  "SUMMARY" : SUMMARY, "usuario" : usuarioObj,"nombre" : nombre})

def main(request):
    if not estaLogeado(request):
            return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])

    formset = PermisoFormSet()
    return render_to_response("edt/main.html", {"form": formset,"usuario": usuarioObj})

   # return render_to_response("edt/main.html", {"user" : usuarioObj},context_instance=RequestContext(request))

def mkmonth_lst():

    if not Permiso.objects.count(): return[]

    year, month = time.localtime()[:2]
    first = Permiso.objects.order_by("fecha_creacion")[0]
    fyear = first.fecha_creacion.year
    fmonth = first.fecha_creacion.month
    months = []

    for y in range(year,fyear-1,-1):
        start,end = 12,0
        if y == year:start = month
        if y == fyear: end = fmonth -1

        for m in range(start,end,-1):
            months.append((y,m,month_name[m]))
        
    return months

def month(request,year,month):
    entrada = Permiso.objects.filter(fecha__year=year,fecha__month=month)
    return render_to_response("edt/permisolst.html",dict(permiso_list=permiso,user=request.user,month=mkmonth_lst(),archive=True))

def verpermiso(request, pk):
     if not estaLogeado(request):
            return redirect("/login")
     else:
         usuarioObj = Usuario.objects.get(id=request.session['usuario'])
         idpermiso = Permiso.objects.get(pk=int(pk))
         permiso = Permiso.objects.get(id=pk)
         if len(permiso.resolucion_set.all()) > 0:
            resolucion = permiso.resolucion_set.all()[0]
         else:
            resolucion = "Sin revisar"
            

     if  usuarioObj.rol.id == 1:
        return render_to_response("edt/verpermiso.html",{ "permiso" : idpermiso,"usuario" : usuarioObj},context_instance=RequestContext(request))

     if  usuarioObj.rol.id == 2:
        return render_to_response("edt/verpermisousuario.html",{ "resolucion" : resolucion,"permiso" : idpermiso,"usuario" : usuarioObj},context_instance=RequestContext(request))


def ingresapermiso(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])     

    if request.method == 'POST':
        formset = PermisoFormSet(request.POST, request.FILES)           
        if formset.is_valid():
            permiso= formset.save(commit=False)
            permiso.usuario = usuarioObj
            permiso.save()
            return redirect("/comprobante/%d"%(permiso.id))

            # do something
    else:
        formset = PermisoFormSet()
    return render_to_response("edt/permiso.html", {"form": formset,})

    
def mostrar_respuesta(request, pk):
    if not estaLogeado(request):
        return redirect("/login")
    else:   
        usuarioObj = Usuario.objects.get(id=request.session['usuario'])
        idresolucion = Resolucion.objects.get(pk=int(pk))
        resolucion = Resolucion.objects.get(id=pk)
        permiso = resolucion.permiso.id    

    
    return render_to_response("edt/resolucion.html",{ "resolucion" : idresolucion,"usuario" : usuarioObj,"permiso" : permiso},context_instance=RequestContext(request)) 

def aprobarRechazar(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])     
    
    if request.POST:
        resu = Resolucion()
        resu.respuesta = request.POST['respuesta']
        resu.resolutor = Usuario.objects.get(id=request.session['usuario'])
        resu.razon = request.POST.get('razon')
        resu.permiso = Permiso.objects.get(id=request.POST['permiso'])  
        resu.save()

        template = loader.get_template('edt/email_respuesta.html')
        context = RequestContext(request, {'nombre' : usuarioObj.nombre,'apellido' : usuarioObj.apellido1,'horas':resu.permiso.horas_solicitadas,'permiso':resu.permiso.id,'respuesta' : resu.respuesta})
        html = template.render(context)
        msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [usuarioObj.correo])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        return redirect("/respuesta/%d"%(resu.id))

def wsGenero(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])    
    sexos = []    
    femenino = len(Usuario.objects.filter(sexo=2))
    masculino = len(Usuario.objects.filter(sexo=1))
    #sexos.append({ 'hombre' : masculino, 'mujer' : femenino})        
    sexos = [['Varones',masculino],['Damas',femenino]]
    #return HttpResponse(json.dumps(sexos))
    return render_to_response("edt/genero.html",{"usuario" : usuarioObj,"sexos" : sexos})

                   
