#!/usr/bin/python
# -*- encoding: utf-8 -*-
from xhtml2pdf import pisa
from easy_pdf.rendering import render_to_pdf_response
from easy_pdf.views import PDFTemplateView
from openpyxl import Workbook
from cal.settings import *
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.generic import View
from reportlab.lib import colors
from reportlab.lib.pagesizes import *
from reportlab.platypus import *
from reportlab.lib.styles import *
from reportlab.lib.units import *
from django.db.models import Max
from dateutil.parser import *
from dateutil.tz import *
from django.utils.dateparse import parse_datetime
from django.utils.dateparse import parse_date
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
from funciones.funciones import *
from forms import *
from datetime import datetime
from dateutil import tz
from collections import Counter
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,FormView,UpdateView
from django.views.generic.base import ContextMixin , TemplateView
from django.db.models import Count, Min, Sum, Avg , F
import time
import calendar
import icalendar
import pytz
import os
import json
import urllib
import time
import tablib


# Generic View de Bitacora
class PermisoListView(ListView):
    template_name = 'edt/bitacora.html'
    context_object_name = 'bitacora'
    paginate_by = 10

    def get_queryset(self):
        return Bitacora.objects.order_by('-fecha')

#-----------------------------------------------------------------------------------------
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
                                return redirect('/main/')
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
                from_zone = tz.gettz('Europe/Paris')
                to_zone = tz.gettz('America/Rio_Branco') # America/Santo_Domingo : -04 desde 25-05 hasta ??? // resto del año America/Santiago - 03 
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

                lista.append({"used": evento.flageado,"id":evento.id, "start":start, "end":end, "multi":0 ,"allDay":False, "extension_id":2})
                data = json.dumps(lista)
            # "title":usuarioObj.nombre+" "+usuarioObj.apellido1 ,
                    
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

@csrf_exempt
def urlcalendario(request):
    if not estaLogeado(request):
                return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    actividad = Actividad.objects.get(id=5)
    usuario_id=request.session['usuario']

    if request.method == 'POST':
        arrayDeEventos = json.loads(request.POST['data-calendario'])  #cargo los id de los eventos seleccionados
        reemplazante = request.POST.get('reemplazante')
        devuelve_horas = request.POST.get('devuelve_horas')
        sueldo = request.POST.get('sueldo')
        comentario = request.POST.get('comentario')
        #comentario = comentario.decode('latin1','replace')# codificacion para tildes
        documento_adjunto = request.POST.get('documento_adjunto')
        #documento_adjunto = documento_adjunto.decode('latin1','replace')# codificacion para tildes
        motivo = request.POST.get('motivo')
                                                                      #en el calendario en formato json a una lista           
        eventos = Evento.objects.filter(id__in=arrayDeEventos) #consulto los eventos en la tabla Eventos segun los Id de la lista

        

    formset = PermisoFormSet(request.POST, request.FILES) 
   
    ############ #########guardado  de   permiso ############################

    if formset.is_valid():
        permiso = formset.save(commit=False)        
        permiso.usuario = usuarioObj
        reemplazante = reemplazante
        permiso.sueldo = sueldo
        permiso.comentario = comentario
        permiso.devuelve_horas = devuelve_horas
        permiso.documenot_adjunto = documento_adjunto
        motivo = motivo
        permiso.save() # guardo los datos de Permiso en la BD

        if len(Permiso.objects.all()) == 0: # verifico si la tabla permisos esta vacia
            ultimopermiso = 1 # si esta vacia le asigno el valor 1
        else:
            #consulto el ultimo registro de la tabla Permiso
            ultimopermiso = Permiso.objects.all().order_by("-id")[0]

        suma = 0
        sumafuncionario = 0
        i = 0
        deltas = []
        deltaf = []  

        for evento in eventos:
            delta = evento.end - evento.start # calculo de la cantidad de horas solicitadas en segundos
            
            if (usuarioObj.estamento.id == 5 or usuarioObj.estamento.id == 4 ):  
                #CALCULO PARA SECUNDARIA
                suma += float(delta.seconds) / 3600 / 0.75 # calculo para  Informes
                deltag = float(delta.seconds) / 3600 / 0.75 # calculo para  Informes
                deltas.append(round(deltag,2))
                sumafuncionario += float(delta.seconds) / 3600  # calculo para  funcionario
                deltafuncionario = float(delta.seconds) / 3600  # calculo para  funcionario
                deltaf.append(round(deltafuncionario,2))  
                  
                suma = round(suma,2) # redondeo a 2 decimales
                evento_en_permiso = Eventos_en_Permisos(numero_evento=evento,numero_permiso=ultimopermiso,deltainforme=deltas[i],deltafuncionario=deltaf[i])
                i += 1
                evento_en_permiso.save()
                

            if (usuarioObj.estamento.id == 2 or usuarioObj.estamento.id == 3):
                #CALCULO DE HORAS PARA PRIMARIA
                suma += float(delta.seconds) / 3600 / 0.75
                deltag = float(delta.seconds) / 3600 / 0.75
                deltas.append(round(deltag,2))
                suma = round(suma,2) # redondeo a 2 decimales
                sumafuncionario += float(delta.seconds) / 3600   # calculo para  funcionario
                deltafuncionario = float(delta.seconds) / 3600  # calculo para  funcionario
                deltaf.append(round(deltafuncionario,2))
                evento_en_permiso = Eventos_en_Permisos(numero_evento=evento,numero_permiso=ultimopermiso,deltainforme=deltas[i],deltafuncionario=deltaf[i])
                i += 1
                evento_en_permiso.save()
                        

            if (usuarioObj.estamento.id == 1 or usuarioObj.estamento.id == 6 or usuarioObj.estamento.id == 7 or usuarioObj.estamento.id == 8):
                #CALCULO DE HORAS PARA ADMINISTRACION
                suma += float(delta.seconds) / 3600  
                deltag = float(delta.seconds) / 3600
                deltas.append(round(deltag,2))
                suma = round(suma,2) # redondeo a 2 decimales
                sumafuncionario = suma

                # sumafuncionario += float(delta.seconds) / 3600   # calculo para  funcionario
                # deltafuncionario = float(delta.seconds) / 3600  # calculo para  funcionario
                # deltaf.append(round(deltafuncionario,2))

                
                evento_en_permiso = Eventos_en_Permisos(numero_evento=evento,numero_permiso=ultimopermiso,deltainforme=deltas[i],deltafuncionario=deltas[i])
                i += 1
                evento_en_permiso.save()

        permiso.horas_solicitadas = suma
        permiso.horas_solicitadas_funcionario =  sumafuncionario
        permiso.save() # guardo suma aca despues de hacer el calculo   

        
        if usuarioObj.jefatura.id == 1 :
            folcpe = Foliocpe(permiso=ultimopermiso)
            folcpe.save()        

        if usuarioObj.jefatura.id == 4 :
            folprimaria = Folioprimaria(permiso=ultimopermiso)
            folprimaria.save()

        if usuarioObj.jefatura.id == 5 :
            folsecundaria = Foliosecundaria(permiso=ultimopermiso)
            folsecundaria.save()

        if usuarioObj.jefatura.id == 7 :
            folmantencion = Foliomantencion(permiso=ultimopermiso)
            folmantencion.save()

        if usuarioObj.jefatura.id == 3 :
            foldirgen = Foliodirgen(permiso=ultimopermiso)
            foldirgen.save()

        if usuarioObj.jefatura.id == 6 :
            folgerencia = Foliogerencia(permiso=ultimopermiso)
            folgerencia.save()


        ###################FOLIOS############################################################################

        cpe = Usuario.objects.values_list("jefatura").filter(jefatura__id=1)
        foliocpe = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=cpe))
    
        primaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=4)
        folioprimaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=primaria))

        secundaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=5)
        foliosecundaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=secundaria))

        mantencion = Usuario.objects.values_list("jefatura").filter(jefatura__id=7)
        foliomantencion = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=mantencion))

        dirgen = Usuario.objects.values_list("jefatura").filter(jefatura__id=3)
        foliosecundaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=dirgen))

        gerencia = Usuario.objects.values_list("jefatura").filter(jefatura__id=6)
        foliosecundaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=gerencia))

        ##########################################################################################################
        #guardo en horas para gestion de devolucion de horas
        
        horas = Horas(horas_solicitadas=sumafuncionario,permiso=ultimopermiso,usuario=usuarioObj)
        horas.save()

        #guardado en bitacora
        bitacora = Bitacora(actividad=actividad,usuario=usuarioObj,permiso=ultimopermiso)            
        bitacora.save()


        #email a funcionario  idpermiso = Permiso.objects.get(pk=int(pk)) 
        template = loader.get_template('edt/email_solicitud.html')
        context = RequestContext(request, {'permiso' : ultimopermiso,'nombre' : usuarioObj.nombre,'apellido' : usuarioObj.apellido1,'horas':permiso.horas_solicitadas,'numero':permiso.id})
        html = template.render(context)
        msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [usuarioObj.correo])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        #email a jefatura
        template = loader.get_template('edt/email_jefatura.html')
        context = RequestContext(request, {'permiso' : ultimopermiso,'jefe' : usuarioObj.jefatura.nombre,'horas':permiso.horas_solicitadas,'numero':permiso.id,'nombre' : usuarioObj.nombre,'apellido' : usuarioObj.apellido1,'rut': usuarioObj.rut,'dv':usuarioObj.dv,'nom_reemplazante':permiso.reemplazante.nombre,'ap_reemplazante':permiso.reemplazante.apellido1,'fecha': permiso.fecha_creacion})
        html = template.render(context)
        msg = EmailMessage('Solicitud de permiso ' , html, 'scpa@cdegaulle.cl', [usuarioObj.jefatura.correo1])
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        
        return redirect("/comprobante/%d"%(ultimopermiso.id))
        #return HttpResponse(sumafuncionario)
    # data = json.dumps({"suma" : suma,"ultimo" : ultimopermiso,"largo":len(eventos),"usuario":usuario_id,"reemplazante" : reemplazante,"devuelve_horas":devuelve_horas})
    # return HttpResponse(data, content_type = "application/json")
    #else:
    #    formset = PermisoFormSet()
    return render_to_response("edt/main.html", {
        "form": formset,
    },context_instance=RequestContext(request)) 



def bitgeneral(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    
    if  usuarioObj.rol.id == 1:
        #permiso = Permiso.objects.all()
        permisos = Permiso.objects.all()
        #resolucion =  Resolucion.objects.all().order_by('-id')
        return render_to_response("edt/bgeneral.html",{"permisos" : permisos,"usuario": usuarioObj},context_instance=RequestContext(request))
    else:
     return redirect("/main")

def bithoras(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    if usuarioObj.rol.id == 1:

        permisos = Permiso.objects.all().order_by("usuario__apellido1")
        estamento = Estamento.objects.all()
        usuarios_filtro = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)
        estamento_filtro = Estamento.objects.all()
        thora = "Seleccione Opción";
         
        if "filtrar" in request.GET:
            if "start" in request.GET and request.GET.get("start") != "":
                permisos = permisos.filter(fecha_creacion__gte=request.GET.get("start"))
                start = request.GET.get("start")


            if "end" in request.GET and request.GET.get("end") != "":
                permisos = permisos.filter(fecha_creacion__lte=request.GET.get("end"))
                end = request.GET.get("end")


            if "persona" in request.GET and request.GET.get("persona") != "0":
                persona = request.GET.get("persona")
                permisos = permisos.filter(usuario=request.GET.get("persona"))
                for usuario in usuarios_filtro:
                    usuario.usuario_activo = usuario.id == int(persona)

            if "estamento" in request.GET and request.GET.get("estamento") != "0":
                estamento = request.GET.get("estamento")
                permisos = permisos.filter(usuario__estamento=request.GET.get("estamento"))
                for estament in estamento_filtro:
                    estament.estamento_activo = estament.id == int(estamento)

            if "thora" in request.GET and request.GET.get("thora") != "0" :
                thora = request.GET.get("thora")
                if thora == 'Horas por Descontar':
                    permisos = permisos.filter(horas__horas_descontar__gt=0)
                if thora == 'Horas por Devolver':
                    permisos = permisos.filter(horas__horas_por_devolver__gt=0)
                if thora == 'Horas Descontadas':
                    permisos = permisos.filter(horas__horas_descontadas__gt=0)
                if thora == 'Horas Devueltas':
                    permisos = permisos.filter(horas__horas_devueltas__gt=0)


        elif "limpiar" in request.GET:
            return redirect("/bhoras")

        #else :
         #   return render_to_response("edt/bhoras.html",data,context_instance=RequestContext(request))

        usuarios = {}
        for permiso in permisos:
            idUsuario = permiso.usuario.id
            if idUsuario not in usuarios:
                usuarios[idUsuario] = {
                     "id" : permiso.usuario.id,
                     "nombre" : permiso.usuario.nombre,
                     "apellido1"  :permiso.usuario.apellido1,
                     "apellido2" : permiso.usuario.apellido2,
                     "estamento" : permiso.usuario.estamento.nombre,
                     "total_horas" : 0,
                     "aprobadas" : 0,
                     "rechazadas" : 0,
                     "devolveracumuladas" : 0,
                     "devueltas" : 0,
                     "saldodevolucion" : 0,
                     "descontaracumuladas" : 0,
                     "descontadas" : 0,
                 }
             
            horas = permiso.horas_set.all()
            if len(horas) == 0:
                 continue
 
            hora = horas[0]
            usuarios[idUsuario]["total_horas"] += hora.horas_solicitadas
            usuarios[idUsuario]["aprobadas"] += hora.horas_aprobadas
            usuarios[idUsuario]["rechazadas"] += hora.horas_rechazadas
            usuarios[idUsuario]["devolveracumuladas"] += hora.horas_por_devolver
            usuarios[idUsuario]["devueltas"] += hora.horas_devueltas
            usuarios[idUsuario]["saldodevolucion"] = usuarios[idUsuario]["devolveracumuladas"] - usuarios[idUsuario]["devueltas"]
            usuarios[idUsuario]["descontaracumuladas"] += hora.horas_descontar
            usuarios[idUsuario]["descontadas"] += hora.horas_descontadas
            usuarios[idUsuario]["saldodescontar"] = usuarios[idUsuario]["descontaracumuladas"] - usuarios[idUsuario]["descontadas"]
             
        usuariosLista = [value for key,value in usuarios.iteritems()]
 
        # headers = ('Nombre','Estamento','Horas solicitadas')
        # excel = []
        # excel = tablib.Dataset()
        # excel.headers = 

        data = {

            "usuario": usuarioObj,
            "usuarios" : usuariosLista,
            "usuarios_filtro" : usuarios_filtro,
            "estamento_filtro" : estamento_filtro,
            "thora" :thora,
            "query_string" : request.META["QUERY_STRING"]
                }

        #Filtros para generar la fecha e el Titulo
        if "filtrar" in request.GET:
            if "start" in request.GET and request.GET.get("start") != "":
                permisos = permisos.filter(fecha_creacion__gte=request.GET.get("start"))
                start = request.GET.get("start")
                inicio = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
                data["inicio"] = inicio
                data["start"] = start 


            if "end" in request.GET and request.GET.get("end") != "":
                permisos = permisos.filter(fecha_creacion__lte=request.GET.get("end"))
                end = request.GET.get("end")
                termino = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
                data["termino"] = termino
                data["end"] = end



        return render_to_response("edt/bhoras.html",data,context_instance=RequestContext(request))

        
        #return HttpResponse(json.dumps(usuarios)) 
        #return HttpResponse(json.dumps(usuariosLista))

    else:
        return redirect("/main")

##########Generacion de informes################

class BitHorasPDF(PDFTemplateView):
    template_name= "edt/bhorasPDF.html"


    def get_context_data(self, **kwargs):
        context =  super(BitHorasPDF,self).get_context_data(
            pagesize="letter",
            title="Informe PDF",
            **kwargs
            )

        usuarioObj = Usuario.objects.get(id=self.request.session['usuario'])
        permisos = Permiso.objects.all().order_by("usuario__apellido1")
        estamento = Estamento.objects.all() 
        usuarios_filtro = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)
        estamento_filtro = Estamento.objects.all()
        thora = "Seleccione Opción";
        
         
        if "filtrar" in self.request.GET:
            if "start" in self.request.GET and self.request.GET.get("start") != "":
                permisos = permisos.filter(fecha_creacion__gte=self.request.GET.get("start"))
                start = self.request.GET.get("start")


            if "end" in self.request.GET and self.request.GET.get("end") != "":
                permisos = permisos.filter(fecha_creacion__lte=self.request.GET.get("end"))
                end = self.request.GET.get("end")


            if "persona" in self.request.GET and self.request.GET.get("persona") != "0":
                persona = self.request.GET.get("persona")
                permisos = permisos.filter(usuario=self.request.GET.get("persona"))
                for usuario in usuarios_filtro:
                    usuario.usuario_activo = usuario.id == int(persona)

            if "estamento" in self.request.GET and self.request.GET.get("estamento") != "0":
                estamento = self.request.GET.get("estamento")
                permisos = permisos.filter(usuario__estamento=self.request.GET.get("estamento"))
                for estament in estamento_filtro:
                    estament.estamento_activo = estament.id == int(estamento)

            if "thora" in self.request.GET and self.request.GET.get("thora") != "0" :
                thora = self.request.GET.get("thora")
                if thora == 'Horas por Descontar':
                    permisos = permisos.filter(horas__horas_descontar__gt=0)
                if thora == 'Horas por Devolver':
                    permisos = permisos.filter(horas__horas_por_devolver__gt=0)
                if thora == 'Horas Descontadas':
                    permisos = permisos.filter(horas__horas_descontadas__gt=0)
                if thora == 'Horas Devueltas':
                    permisos = permisos.filter(horas__horas_devueltas__gt=0)

        usuarios = {}
        for permiso in permisos:
            idUsuario = permiso.usuario.id
            if idUsuario not in usuarios:
                usuarios[idUsuario] = {
                     "id" : permiso.usuario.id,
                     "nombre" : permiso.usuario.nombre,
                     "apellido1"  :permiso.usuario.apellido1,
                     "apellido2" : permiso.usuario.apellido2,
                     "estamento" : permiso.usuario.estamento.nombre,
                     "total_horas" : 0,
                     "aprobadas" : 0,
                     "rechazadas" : 0,
                     "devolveracumuladas" : 0,
                     "devueltas" : 0,
                     "saldodevolucion" : 0,
                     "descontaracumuladas" : 0,
                     "descontadas" : 0,
                 }
             
            horas = permiso.horas_set.all()
            if len(horas) == 0:
                 continue
 
            hora = horas[0]
            usuarios[idUsuario]["total_horas"] += hora.horas_solicitadas
            usuarios[idUsuario]["aprobadas"] += hora.horas_aprobadas
            usuarios[idUsuario]["rechazadas"] += hora.horas_rechazadas
            usuarios[idUsuario]["devolveracumuladas"] += hora.horas_por_devolver
            usuarios[idUsuario]["devueltas"] += hora.horas_devueltas
            usuarios[idUsuario]["saldodevolucion"] = usuarios[idUsuario]["devolveracumuladas"] - usuarios[idUsuario]["devueltas"]
            usuarios[idUsuario]["descontaracumuladas"] += hora.horas_descontar
            usuarios[idUsuario]["descontadas"] += hora.horas_descontadas
            usuarios[idUsuario]["saldodescontar"] = usuarios[idUsuario]["descontaracumuladas"] - usuarios[idUsuario]["descontadas"]
             
        usuariosLista = [value for key,value in usuarios.iteritems()]
 
      

        context = {

            "usuario": usuarioObj,
            "usuarios" : usuariosLista,
            "usuarios_filtro" : usuarios_filtro,
            "estamento_filtro" : estamento_filtro,
            "thora" :thora,            
                }
        context['hoy'] =  datetime.now()
        #Filtros para generar la fecha e el Titulo
        
        if "filtrar" in self.request.GET:
            if "start" in self.request.GET and self.request.GET.get("start") != "":
                permisos = permisos.filter(fecha_creacion__gte=self.request.GET.get("start"))
                start = self.request.GET.get("start")
                inicio = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
                context["inicio"] = inicio
                context["start"] = start 


            if "end" in self.request.GET and self.request.GET.get("end") != "":
                permisos = permisos.filter(fecha_creacion__lte=self.request.GET.get("end"))
                end = self.request.GET.get("end")
                termino = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
                context["termino"] = termino
                context["end"] = end
        
        return context


class BitHorasExcel(TemplateView):
    """docstring for BitHorasExcel"""
    def get(self, request, *args, **kwargs):

        usuarioObj = Usuario.objects.get(id=self.request.session['usuario'])
        permisos = Permiso.objects.all().order_by("usuario__apellido1")
        estamento = Estamento.objects.all() 
        usuarios_filtro = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)
        estamento_filtro = Estamento.objects.all()
        thora = "Seleccione Opción";
        
         
        if "filtrar" in self.request.GET:
            if "start" in self.request.GET and self.request.GET.get("start") != "":
                permisos = permisos.filter(fecha_creacion__gte=self.request.GET.get("start"))
                start = self.request.GET.get("start")


            if "end" in self.request.GET and self.request.GET.get("end") != "":
                permisos = permisos.filter(fecha_creacion__lte=self.request.GET.get("end"))
                end = self.request.GET.get("end")


            if "persona" in self.request.GET and self.request.GET.get("persona") != "0":
                persona = self.request.GET.get("persona")
                permisos = permisos.filter(usuario=self.request.GET.get("persona"))
                for usuario in usuarios_filtro:
                    usuario.usuario_activo = usuario.id == int(persona)

            if "estamento" in self.request.GET and self.request.GET.get("estamento") != "0":
                estamento = self.request.GET.get("estamento")
                permisos = permisos.filter(usuario__estamento=self.request.GET.get("estamento"))
                for estament in estamento_filtro:
                    estament.estamento_activo = estament.id == int(estamento)

            if "thora" in self.request.GET and self.request.GET.get("thora") != "0" :
                thora = self.request.GET.get("thora")
                if thora == 'Horas por Descontar':
                    permisos = permisos.filter(horas__horas_descontar__gt=0)
                if thora == 'Horas por Devolver':
                    permisos = permisos.filter(horas__horas_por_devolver__gt=0)
                if thora == 'Horas Descontadas':
                    permisos = permisos.filter(horas__horas_descontadas__gt=0)
                if thora == 'Horas Devueltas':
                    permisos = permisos.filter(horas__horas_devueltas__gt=0)

        usuarios = {}
        for permiso in permisos:
            idUsuario = permiso.usuario.id
            if idUsuario not in usuarios:
                usuarios[idUsuario] = {
                     "id" : permiso.usuario.id,
                     "nombre" : permiso.usuario.nombre,
                     "apellido1"  :permiso.usuario.apellido1,
                     "apellido2" : permiso.usuario.apellido2,
                     "estamento" : permiso.usuario.estamento.nombre,
                     "total_horas" : 0,
                     "aprobadas" : 0,
                     "rechazadas" : 0,
                     "devolveracumuladas" : 0,
                     "devueltas" : 0,
                     "saldodevolucion" : 0,
                     "descontaracumuladas" : 0,
                     "descontadas" : 0,
                 }
             
            horas = permiso.horas_set.all()
            if len(horas) == 0:
                 continue
 
            hora = horas[0]
            usuarios[idUsuario]["total_horas"] += hora.horas_solicitadas
            usuarios[idUsuario]["aprobadas"] += hora.horas_aprobadas
            usuarios[idUsuario]["rechazadas"] += hora.horas_rechazadas
            usuarios[idUsuario]["devolveracumuladas"] += hora.horas_por_devolver
            usuarios[idUsuario]["devueltas"] += hora.horas_devueltas
            usuarios[idUsuario]["saldodevolucion"] = usuarios[idUsuario]["devolveracumuladas"] - usuarios[idUsuario]["devueltas"]
            usuarios[idUsuario]["descontaracumuladas"] += hora.horas_descontar
            usuarios[idUsuario]["descontadas"] += hora.horas_descontadas
            usuarios[idUsuario]["saldodescontar"] = usuarios[idUsuario]["descontaracumuladas"] - usuarios[idUsuario]["descontadas"]
             
        usuariosLista = [value for key,value in usuarios.iteritems()]

        hoy = datetime.now()
        #Creamos el libro de trabajo
        wb= Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'INFORME DE HORAS'
        ws['B1'] = 'INFORME DE HORAS'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        #Creamos los encabezados desde la celda B3 hasta la L3
        ws['B3'] = 'NOMBRE'
        ws['C3'] = 'ESTAMENTO'
        ws['D3'] = 'HORAS SOLICITADAS'
        ws['E3'] = 'HORAS APROBADAS'
        ws['F3'] = 'HORAS RECHAZADAS'
        ws['G3'] = 'HORAS A RECUPERAR ACUMULADAS'
        ws['H3'] = 'HORAS RECUPERADAS'
        ws['I3'] = 'SALDO DE HORAS POR RECUPERAR'
        ws['J3'] = 'HORAS POR DESCONTAR ACUMULADAS'
        ws['K3'] = 'HORAS DESCONTADAS'
        ws['L3'] = 'SALDO HORAS POR DESCONTAR'
        cont=4
        for usuario in usuariosLista:

            ws.cell(row=cont,column=2).value = usuario["apellido1"]+" "+usuario["apellido2"]+" "+usuario["nombre"]
            ws.cell(row=cont,column=3).value = usuario["estamento"]
            ws.cell(row=cont,column=4).value = usuario["total_horas"]
            ws.cell(row=cont,column=5).value = usuario["aprobadas"]
            ws.cell(row=cont,column=6).value = usuario["rechazadas"]
            ws.cell(row=cont,column=7).value = usuario["devolveracumuladas"]
            ws.cell(row=cont,column=8).value = usuario["devueltas"]
            ws.cell(row=cont,column=9).value = usuario["saldodevolucion"]  
            ws.cell(row=cont,column=10).value = usuario["descontaracumuladas"]
            ws.cell(row=cont,column=11).value = usuario["descontadas"]
            ws.cell(row=cont,column=12).value = usuario["saldodescontar"]
            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="informe_de_horas.xlsx"
        response = HttpResponse(content_type="application/ms-excel") 
        contenido = "attachment; filename={0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response     
        



##############FIN GENERACION DE INFORMES ###################################
def permisosusuario(request,pk):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    permisos = Permiso.objects.filter(usuario__id=pk)
    bitacoras = Bitacora.objects.filter(permiso__usuario__id=pk)

    data = {

        "usuario" : usuarioObj,
        "permisos" : permisos,
        "months" : mkmonth_lst(),   
        "bitacoras" : bitacoras,

    }


    return render_to_response("edt/permisosusuariolst.html",data,context_instance=RequestContext(request))


def bitfuncionario(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    
    #if  usuarioObj.rol.id == 1:
        
    permisos = Permiso.objects.filter(usuario=usuarioObj.id).annotate()
    #resolucion =  Resolucion.objects.all().order_by('-id')
    return render_to_response("edt/bfuncionario.html",{"permisos" : permisos,"usuario": usuarioObj},context_instance=RequestContext(request))
    # else:
    #  return redirect("/main")        

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
            
                
            formset = DocumentFormSet()
            return render_to_response("edt/index.html", {"form": formset,"usuario": usuarioObj},context_instance=RequestContext(request))
        else:
                return redirect("/main") 

def permisolst(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    anulados = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
    rechazados = Resolucion.objects.values_list("permiso").filter(respuesta='R')
    gerencia = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b__gte=2).filter(usuario__jefatura=6)
    dirgen = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b__gte=2).filter(usuario__jefatura=3)

    permisos = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b__lte=2).exclude(id__in=dirgen).exclude(id__in=gerencia).exclude(id__in=anulados).exclude(id__in=rechazados).order_by("-fecha_creacion") 
    

    bitacoras = Bitacora.objects.all()


    cpe = Usuario.objects.values_list("jefatura").filter(jefatura__id=1)
    foliocpe = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=cpe))
    
    primaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=4)
    folioprimaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=primaria))

    secundaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=5)
    foliosecundaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=secundaria))    

    if  usuarioObj.rol.nivel_acceso == 0:

        
        estamento = Estamento.objects.all()
        usuarios_filtro = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)
        estamento_filtro = Estamento.objects.all()

        if "filtrar" in request.GET:           

            if "persona" in request.GET and request.GET.get("persona") != "0":
                persona = request.GET.get("persona")
                permisos = permisos.filter(usuario=request.GET.get("persona"))
                for usuario in usuarios_filtro:
                    usuario.usuario_activo = usuario.id == int(persona)

            if "estamento" in request.GET and request.GET.get("estamento") != "0":
                estamento = request.GET.get("estamento")
                permisos = permisos.filter(usuario__estamento=request.GET.get("estamento"))
                for estament in estamento_filtro:
                    estament.estamento_activo = estament.id == int(estamento)   
        elif "limpiar" in request.GET:
            return redirect("/permisolst")       
        paginator = Paginator(permisos,30)
        
        try: pagina = int(request.GET.get("page",'1'))
        except ValueError: pagina = 1
            
        try:
            permisos = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            permisos = paginator.page(paginator.num_pages)


        data = {
                 "estamento":estamento,
                 "foliocpe":foliocpe,
                 "folioprimaria" :folioprimaria,
                 "foliosecundaria" :foliosecundaria ,
                 "permisos": permisos,
                 "usuario" : usuarioObj,
                 "permisos_list" : permisos.object_list,
                 "months" : mkmonth_lst(),
                 "usuarios_filtro" : usuarios_filtro,
                 "estamento_filtro" : estamento_filtro,
                 "bitacoras" : bitacoras,
                 }


        return render_to_response("edt/permisolst.html",data)
        #return HttpResponse(administracion)

    else:
        #if     usuarioObj.username == request.session['usuario']:
        if  usuarioObj.rol.nivel_acceso == 1:
            ids = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
            permiso = Permiso.objects.annotate(num_b=Count('resolucion')).filter(usuario=usuarioObj.id).exclude(id__in=ids).order_by("-fecha_creacion")
            

            paginator = Paginator(permiso,10)       
            try: pagina = int(request.GET.get("page",'1'))
            except ValueError: pagina = 1       
            try:
                permiso = paginator.page(pagina)
            except (InvalidPage, EmptyPage):
                permiso = paginator.page(paginator.num_pages)

        data = {
                 "foliocpe":foliocpe,
                 "folioprimaria" :folioprimaria,
                 "foliosecundaria" :foliosecundaria ,
                 "permisos": permiso,
                 "usuario" : usuarioObj,
                 "permisos_list" : permiso.object_list,
                 "months" : mkmonth_lst(),
               }
            
        return render_to_response("edt/permisolst.html",data)


def anuladoslst(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    anulados = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
    rechazados = Resolucion.objects.values_list("permiso").filter(respuesta='R')
    gerencia = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b__lte=2).filter(usuario__jefatura=6)
    dirgen = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b__lte=2).filter(usuario__jefatura=3)

    permisos = Permiso.objects.filter(id__in=anulados)
    

    bitacoras = Bitacora.objects.all()


    cpe = Usuario.objects.values_list("jefatura").filter(jefatura__id=1)
    foliocpe = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=cpe))
    
    primaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=4)
    folioprimaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=primaria))

    secundaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=5)
    foliosecundaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=secundaria))    

    if  usuarioObj.rol.nivel_acceso == 0:

        
        estamento = Estamento.objects.all()
        usuarios_filtro = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)
        estamento_filtro = Estamento.objects.all()

        if "filtrar" in request.GET:           

            if "persona" in request.GET and request.GET.get("persona") != "0":
                persona = request.GET.get("persona")
                permisos = permisos.filter(usuario=request.GET.get("persona"))
                for usuario in usuarios_filtro:
                    usuario.usuario_activo = usuario.id == int(persona)

            if "estamento" in request.GET and request.GET.get("estamento") != "0":
                estamento = request.GET.get("estamento")
                permisos = permisos.filter(usuario__estamento=request.GET.get("estamento"))
                for estament in estamento_filtro:
                    estament.estamento_activo = estament.id == int(estamento)   
        elif "limpiar" in request.GET:
            return redirect("/permisolst")       
        paginator = Paginator(permisos,30)
        
        try: pagina = int(request.GET.get("page",'1'))
        except ValueError: pagina = 1
            
        try:
            permisos = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            permisos = paginator.page(paginator.num_pages)


        data = {
                 "estamento":estamento,
                 "foliocpe":foliocpe,
                 "folioprimaria" :folioprimaria,
                 "foliosecundaria" :foliosecundaria ,
                 "permisos": permisos,
                 "usuario" : usuarioObj,
                 "permisos_list" : permisos.object_list,
                 "months" : mkmonth_lst(),
                 "usuarios_filtro" : usuarios_filtro,
                 "estamento_filtro" : estamento_filtro,
                 "bitacoras" : bitacoras,
                 }


        return render_to_response("edt/anuladoslst.html",data)
        #return HttpResponse(administracion)

    else:
        #if     usuarioObj.username == request.session['usuario']:
        if  usuarioObj.rol.nivel_acceso == 1:
        
            anulados = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
            permiso = Permiso.objects.filter(id__in=anulados)
            

            paginator = Paginator(permiso,10)       
            try: pagina = int(request.GET.get("page",'1'))
            except ValueError: pagina = 1       
            try:
                permiso = paginator.page(pagina)
            except (InvalidPage, EmptyPage):
                permiso = paginator.page(paginator.num_pages)


            
        data = {
                 "foliocpe":foliocpe,
                 "folioprimaria" :folioprimaria,
                 "foliosecundaria" :foliosecundaria ,
                 "permisos": permiso,
                 "usuario" : usuarioObj,
                 "permisos_list" : permiso.object_list,
                 "months" : mkmonth_lst(),
               }
            
        return render_to_response("edt/anuladoslst.html",data)

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

    permisos = Permiso.objects.filter(usuario=usuarioObj.id)
    bitacoras = Bitacora.objects.all()
    formset = PermisoFormSet()

    usuarios = {}
    for permiso in permisos:
        idUsuario = permiso.usuario.id
        if idUsuario not in usuarios:
            usuarios[idUsuario] = {
                 "id" : permiso.usuario.id,
                 "nombre" : permiso.usuario.nombre,
                 "apellido1"  :permiso.usuario.apellido1,
                 "apellido2" : permiso.usuario.apellido2,
                 "estamento" : permiso.usuario.estamento.nombre,
                 "total_horas" : 0,
                 "aprobadas" : 0,
                 "rechazadas" : 0,
                 "devolveracumuladas" : 0,
                 "devueltas" : 0,
                 "saldodevolucion" : 0,
                 "descontaracumuladas" : 0,
                 "descontadas" : 0,
             }
         
        horas = permiso.horas_set.all()
        if len(horas) == 0:
             continue

        hora = horas[0]
        usuarios[idUsuario]["total_horas"] += hora.horas_solicitadas
        usuarios[idUsuario]["aprobadas"] += hora.horas_aprobadas
        usuarios[idUsuario]["rechazadas"] += hora.horas_rechazadas
        usuarios[idUsuario]["devolveracumuladas"] += hora.horas_por_devolver
        usuarios[idUsuario]["devueltas"] += hora.horas_devueltas
        usuarios[idUsuario]["saldodevolucion"] = usuarios[idUsuario]["devolveracumuladas"] - usuarios[idUsuario]["devueltas"]
        usuarios[idUsuario]["descontaracumuladas"] += hora.horas_descontar
        usuarios[idUsuario]["descontadas"] += hora.horas_descontadas
        usuarios[idUsuario]["saldodescontar"] = usuarios[idUsuario]["descontaracumuladas"] - usuarios[idUsuario]["descontadas"]
         
    usuariosLista = [value for key,value in usuarios.iteritems()]
   
    data = {
            "form": formset,
            "usuario": usuarioObj,
            "permisos" : permisos ,
            "bitacoras" : bitacoras,
            "usuarios" : usuariosLista,
           }

    
    return render_to_response("edt/main.html", data)
   # return render_to_response("edt/main.html", {"user" : usuarioObj},context_instance=RequestContext(request))

def descontar(request):
    if not estaLogeado(request):
            return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])    
    revisados = Resolucion.objects.values_list('permiso')        
    anulados = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
    rechazados = Resolucion.objects.values_list("permiso").filter(respuesta='R')
    sindevolucion= Permiso.objects.filter(devuelve_horas='N')
   

    if  usuarioObj.rol.nivel_acceso == 0: 
        usuarios = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)

        if request.method == 'POST':
            if "usuario" in request.POST and request.POST.get("usuario") != "":
                seleccionado = request.POST.get("usuario")
                permisos  = Permiso.objects.filter(usuario=seleccionado)
                horas = Horas.objects.filter(permiso__usuario=seleccionado)
                horas = horas.exclude(permiso__id__in=anulados)
                horas = horas.filter(permiso__id__in=revisados)
                horas = horas.exclude(permiso__id__in=rechazados)
               
                for user in usuarios:
                    user.usuario_activo = user.id == int(seleccionado)

            if "horasdescontar" in request.POST and request.POST.get("horasdescontar") != "":
                permisoid = request.POST.get("permisoid")
                horasdescontar = request.POST.get("horasdescontar")
                permisodesc  = Permiso.objects.get(id=permisoid)
                if len(permisodesc.horas_set.all()) > 0:
                    horas = Horas.objects.get(permiso=permisoid)
                    horas.horas_descontadas = horasdescontar
                    horas.save()
                    data = {
                        "usuario": usuarioObj,
                        "horasdescontar" : horasdescontar,
                        "permiso" : permisodesc,

                    }

                    return render_to_response("edt/horasdescontadas.html",data,context_instance=RequestContext(request))
                    #return HttpResponse(horasdescontar)
                else:
                    return HttpResponse("mayor que 0")    

                return HttpResponse(horasdescontar)    

            return render_to_response("edt/descontarhoras.html",{"horas" : horas,"usuarios" : usuarios,"permisos":permisos,"usuario"  :usuarioObj },context_instance=RequestContext(request))    

            #return HttpResponse(permisos)
            #return redirect('/devueltas/%d'%(horas.id))
        else:                
                
            return render_to_response("edt/descontarhoras.html",{"anulados" : anulados,"usuarios": usuarios,"usuario": usuarioObj},context_instance=RequestContext(request))
    
    else:
        return redirect("/main")

def devuelvehoras(request):
    if not estaLogeado(request):
            return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    revisados = Resolucion.objects.values_list('permiso')        
    anulados = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
    rechazados = Resolucion.objects.values_list("permiso").filter(respuesta='R')
    sindevolucion= Permiso.objects.filter(devuelve_horas='N')
   

    if  usuarioObj.rol.nivel_acceso == 0: 
        usuarios = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)

        if request.method == 'POST':
            if "usuario" in request.POST and request.POST.get("usuario") != "":
                seleccionado = request.POST.get("usuario")
                permisos  = Permiso.objects.filter(usuario=seleccionado)
                horas = Horas.objects.filter(permiso__usuario=seleccionado)
                horas = horas.exclude(permiso__id__in=anulados)
                horas = horas.filter(permiso__id__in=revisados)
                horas = horas.exclude(permiso__id__in=rechazados)
                horas = horas.exclude(permiso__id__in=sindevolucion)

                for user in usuarios:
                    user.usuario_activo = user.id == int(seleccionado)

            if "horasdevolver" in request.POST and request.POST.get("horasdevolver") != "":
                permisoid = request.POST.get("permisoid")
                horasdevueltas = request.POST.get("horasdevolver")
                permisodesc  = Permiso.objects.get(id=permisoid)
                if len(permisodesc.horas_set.all()) > 0:                    
                    horas = Horas.objects.get(permiso=permisoid)                    
                    horas.horas_por_devolver = horas.horas_por_devolver - horasdevueltas
                    horas.horas_devueltas = horasdevueltas
                    horas.save()
                    data = {
                        "usuario": usuarioObj,
                        "horasdevueltas" : horasdevueltas,
                        "permiso" : permisodesc,                        
                    }

                    return render_to_response("edt/devueltas.html",data,context_instance=RequestContext(request))
                    #return HttpResponse(horasdescontar)
                else:
                    return HttpResponse("mayor que 0")    

                return HttpResponse(horasdevolver)    

            return render_to_response("edt/devuelvehoras.html",{"horas" : horas,"usuarios" : usuarios,"permisos":permisos,"usuario"  :usuarioObj },context_instance=RequestContext(request))    

            #return HttpResponse(permisos)
            #return redirect('/devueltas/%d'%(horas.id))
        else:                
                
            #return HttpResponse(anulados)
            return render_to_response("edt/devuelvehoras.html",{"anulados" : anulados,"usuarios": usuarios,"usuario": usuarioObj},context_instance=RequestContext(request))
    
    else:
        return redirect("/main")
   
def devueltas(request,pk):
    if not estaLogeado(request):
            return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])

    horas = Horas.objects.get(pk=int(pk))

    return render_to_response("edt/devueltas.html",{"horas": horas,"usuario": usuarioObj},context_instance=RequestContext(request))

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
         permiso = Permiso.objects.get(id=pk)
         permiso_formset = PermisoFormSet(instance=permiso)
         usuarioObj = Usuario.objects.get(id=request.session['usuario'])
         idpermiso = Permiso.objects.get(pk=int(pk))         
         if len(permiso.resolucion_set.all()) > 0:
            resolucion = permiso.resolucion_set.all()[0]
         else:
            resolucion = "Sin revisar"
            

     if  usuarioObj.rol.id == 1:
        if len(permiso.resolucion_set.all()) > 0:
            revisiones = Resolucion.objects.filter(permiso=permiso)
        else:
            revisiones = ""            
        #return HttpResponse(resolucion)
        return render_to_response("edt/verpermiso.html",{ "revisiones" : revisiones,"permiso_formset" : permiso_formset,"permiso" : idpermiso,"usuario" : usuarioObj},context_instance=RequestContext(request))

     if  usuarioObj.rol.id == 2:
        return render_to_response("edt/verpermisousuario.html",{ "resolucion" : resolucion,"permiso" : idpermiso,"usuario" : usuarioObj},context_instance=RequestContext(request))

def verpermiso2(request, pk):
     if not estaLogeado(request):
            return redirect("/login")
     else:
         permiso = Permiso.objects.get(id=pk)
         permiso_formset = PermisoFormSet(instance=permiso)
         usuarioObj = Usuario.objects.get(id=request.session['usuario'])
         idpermiso = Permiso.objects.get(pk=int(pk))         
         if len(permiso.resolucion_set.all()) > 0:
            resolucion = permiso.resolucion_set.all()[0]
         else:
            resolucion = "Sin revisar"
            

     if  usuarioObj.rol.id == 1:
        if len(permiso.resolucion_set.all()) > 0:
            revisiones = Resolucion.objects.filter(permiso=permiso)
        else:
            revisiones = ""            
        #return HttpResponse(resolucion)
        return render_to_response("edt/verpermiso2.html",{ "revisiones" : revisiones,"permiso_formset" : permiso_formset,"permiso" : idpermiso,"usuario" : usuarioObj},context_instance=RequestContext(request))

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

        if request.POST['respuesta'] == 'A' :
            permiso = Permiso.objects.get(id=request.POST['permiso'])
            permiso.comentario = request.POST.get('comentario')
            permiso.sueldo = request.POST.get('sueldo')
            permiso.devuelve_horas = request.POST.get('devuelve_horas')
            permiso.save()
            horas = Horas.objects.get(permiso=permiso)            
            #horas = Horas(permiso=permiso,usuario=permiso.usuario,horas_solicitadas=permiso.horas_solicitadas,horas_aprobadas=permiso.horas_solicitadas,horas_por_devolver=permiso.horas_solicitadas)
            horas.permiso = permiso
            horas.usuario = permiso.usuario
            horas.horas_solicitadas = permiso.horas_solicitadas
            horas.horas_aprobadas = permiso.horas_solicitadas
            if permiso.devuelve_horas == 'S':
                horas.horas_por_devolver = permiso.horas_solicitadas                

            if (permiso.devuelve_horas == 'N' and permiso.sueldo == 'S'):          
                horas.horas_descontar = permiso.horas_solicitadas
                horas.horas_por_devolver = 0

            if (permiso.devuelve_horas == 'N' and permiso.sueldo == 'C'):
                horas.horas_descontar = 0


            horas.save()

            form = PermisoFormSetEdit(request.POST,instance=permiso)
            if form.is_valid():
                form.save()
            actividad = Actividad.objects.get(id=2)
            resu = procesa_resolucion(request,actividad,usuarioObj)
            

        if request.POST['respuesta'] == 'R' :
            permiso = Permiso.objects.get(id=request.POST['permiso'])
            horas = Horas.objects.get(permiso=permiso)
            #horas = Horas(permiso=permiso,usuario=permiso.usuario,horas_solicitadas=permiso.horas_solicitadas,horas_rechazadas=permiso.horas_solicitadas)
            horas.permiso = permiso
            horas.usuario = permiso.usuario
            horas.horas_horas_solicitadas = permiso.horas_solicitadas
            horas.horas_rechazadas = permiso.horas_solicitadas
            horas.save()
            actividad = Actividad.objects.get(id=3)
            resu = procesa_resolucion(request,actividad,usuarioObj)        


        return redirect("/respuesta/%d"%(resu.id))


def anularlst(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])
    anulados = Bitacora.objects.values_list("permiso").filter(actividad__id=4).distinct()
    rechazados = Resolucion.objects.values_list("permiso").filter(respuesta='R')

    

    permisos = Permiso.objects.annotate(num_b=Count('resolucion')).filter(num_b__lte=5).exclude(id__in=anulados).exclude(id__in=rechazados).order_by("-fecha_creacion") 

    cpe = Usuario.objects.values_list("jefatura").filter(jefatura__id=1)
    foliocpe = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=cpe))
    
    primaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=4)
    folioprimaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=primaria))

    secundaria = Usuario.objects.values_list("jefatura").filter(jefatura__id=5)
    foliosecundaria = len(Permiso.objects.annotate(sec=Count('usuario')).filter(usuario__jefatura=secundaria))

    if  usuarioObj.rol.nivel_acceso == 0:

        
        estamento = Estamento.objects.all()
        usuarios_filtro = Usuario.objects.all().exclude(permiso__horas__horas_solicitadas=None)
        estamento_filtro = Estamento.objects.all()

        if "filtrar" in request.GET:           

            if "persona" in request.GET and request.GET.get("persona") != "0":
                persona = request.GET.get("persona")
                permisos = permisos.filter(usuario=request.GET.get("persona"))
                for usuario in usuarios_filtro:
                    usuario.usuario_activo = usuario.id == int(persona)

            if "estamento" in request.GET and request.GET.get("estamento") != "0":
                estamento = request.GET.get("estamento")
                permisos = permisos.filter(usuario__estamento=request.GET.get("estamento"))
                for estament in estamento_filtro:
                    estament.estamento_activo = estament.id == int(estamento)   
        elif "limpiar" in request.GET:
            return redirect("/anularlst")  

        paginator = Paginator(permisos,30)
        
        try: pagina = int(request.GET.get("page",'1'))
        except ValueError: pagina = 1
            
        try:
            permisos = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            permisos = paginator.page(paginator.num_pages)


        data = {
                 "estamento":estamento,
                 "foliocpe":foliocpe,
                 "folioprimaria" :folioprimaria,
                 "foliosecundaria" :foliosecundaria ,
                 "permisos": permisos,
                 "usuario" : usuarioObj,
                 "permisos_list" : permisos.object_list,
                 "months" : mkmonth_lst(),
                 "usuarios_filtro" : usuarios_filtro,
                 "estamento_filtro" : estamento_filtro,
                 }


        return render_to_response("edt/anularlst.html",data)
    else:
        return redirect("/main")

def anulapermiso(request,pk):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])

    idpermiso = Permiso.objects.get(pk=int(pk))
    permiso = Permiso.objects.get(id=pk)

    return render_to_response("edt/anulapermiso.html",{ "permiso" : idpermiso,"usuario" : usuarioObj},context_instance=RequestContext(request))

def anula(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])

    if request.POST:        

        if request.POST.get('anular') == 'Anulado' :

            permiso_id = request.POST.get('permiso')
            motivo = request.POST.get('motivo')
            #guardo en permiso reseteando las horas a 0 
            permiso = Permiso.objects.get(id=permiso_id)
            permiso.horas_solicitadas = 0
            permiso.horas_solicitadas_funcionario = 0
            #guardo en Bitacora
            actividad = Actividad.objects.get(id=4)
            bitacora = Bitacora(actividad=actividad,usuario=usuarioObj,permiso=permiso)            
            bitacora.save()
            #guardo en Anulado para el registro de los permisos anulados
            anulado = Anulado(permiso=permiso,anuladopor=usuarioObj,motivo=motivo)
            anulado.save()

            #arrayAnular = []

            para_anular = Eventos_en_Permisos.objects.filter(numero_permiso=permiso) 

            for evento_anulado in para_anular :#aqui
                anulados = Eventos_en_Permisos_Anulados(evento=evento_anulado.numero_evento,permiso=permiso,deltafuncionario=evento_anulado.deltafuncionario,deltainforme=evento_anulado.deltainforme)
                anulados.save()
                
            
            #libero los eventos para poder ser reutilizados
            eventos = Eventos_en_Permisos.objects.filter(numero_permiso=permiso).delete()            
            #guardo en horas reseteando las horas_solicitadas a 0 
            horas = Horas.objects.get(permiso=permiso)
            horas.horas_solicitadas = 0
            horas.horas_descontar = 0
            horas.horas_por_devolver = 0
            horas.horas_aprobadas = 0 
            horas.save()


        if request.POST.get('cancelar') == 'Cancelado':

            return redirect("/anularlst")    
            
    return redirect("/anulado/%d"%(bitacora.id))


def mostrar_anulado(request,pk):
    if not estaLogeado(request):
        return redirect("/login")

    else:   
        usuarioObj = Usuario.objects.get(id=request.session['usuario'])
        idbitacora = Bitacora.objects.get(pk=int(pk))
        bitacora = Bitacora.objects.get(id=pk)
        permiso = bitacora.permiso.id    

    
    return render_to_response("edt/anulado.html",{ "bitacora" : bitacora, "usuario" : usuarioObj,"permiso" : permiso},context_instance=RequestContext(request)) 

def horas(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario']) 

    if  usuarioObj.rol.nivel_acceso == 0:

        #Calculo de Horas Solicitadas, Devueltas por Usuario
        horas =  Usuario.objects.annotate(horas_sol=Sum("horas__horas_solicitadas")).annotate(horas_dev=Sum("horas__horas_devueltas")).annotate(total=F('horas_sol') - F('horas_dev')).annotate(h=Count('horas')).exclude(h=0).order_by("apellido1")

        paginator = Paginator(horas,10)       
        try: pagina = int(request.GET.get("page",'1'))
        except ValueError: pagina = 1       
        try:
            permiso = paginator.page(pagina)
        except (InvalidPage, EmptyPage):
            permiso = paginator.page(paginator.num_pages)

        return render_to_response("edt/horas.html",{"usuario": usuarioObj,"horas":horas,"permisoObj_list" : permiso.object_list,"months" : mkmonth_lst()},context_instance=RequestContext(request))
    else:
        return redirect("/main")

def wsGenero(request):
    if not estaLogeado(request): 
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])

    # 3 formas de generar arrays====================================    
    sexos = []
    listausr = []    
    femenino = len(Usuario.objects.filter(sexo=2))
    masculino = len(Usuario.objects.filter(sexo=1))
        
    sexos = [['Varones',masculino],['Damas',femenino]]

    for usuario in Usuario.objects.all():       
        listausr.append([usuario.nombre,usuario.apellido1])

   #generacion de array desde una queryset
    data = Usuario.objects.values("jefatura__nombre").annotate(cantidad=Count("jefatura__id"))
    
    jefaturas = [ [ x["jefatura__nombre"] , x["cantidad"] ] for x in data]    
        

    #return HttpResponse(json.dumps(sexos))
    return render_to_response("edt/genero.html",{"usuario" : usuarioObj,"sexos" : sexos,"usuarios" : json.dumps(listausr),"jefaturas" : json.dumps(jefaturas)})

def wsJefaturas(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])        
   
    jefaturas = []
    CPE = len(Usuario.objects.filter(jefatura=1))
    PrimSecu = len(Usuario.objects.filter(jefatura=2))
    Dirgen = len(Usuario.objects.filter(jefatura=3))
    Primaria = len(Usuario.objects.filter(jefatura=4))
    Secundaria = len(Usuario.objects.filter(jefatura=5))
    Gerencia = len(Usuario.objects.filter(jefatura=6))
    Mantencion = len(Usuario.objects.filter(jefatura=7))
 
    jefaturas = [['CPE',CPE],['D. Primaria/D. Secundaria',PrimSecu ],['Dir. General', Dirgen],['Primaria',Primaria],['Secundaria',Secundaria],['Gerencia',Gerencia],['Mantencion',Mantencion]]
    # #generacion de array desde una queryset
    # data = Usuario.objects.values("jefatura__nombre").annotate(cantidad=Count("jefatura"))   
    # jefaturas = [ [ x["jefatura__nombre"] , x["cantidad"] ] for x in data]    
        

    #return HttpResponse(json.dumps(jefaturas))
    return render_to_response("edt/jefaturas.html",{"usuario" : usuarioObj,"jefaturas" : jefaturas })

def wsEdades(request):
    if not estaLogeado(request):
        return redirect("/login")
    usuarioObj = Usuario.objects.get(id=request.session['usuario'])        
   
    hoy = datetime.now()
    
    data = Usuario.objects.values("fecha_nac") #seleccion de fechas de nacimiento  
    edad = [  hoy.year - x["fecha_nac"].year  for x in data] #calculo de edad de funcionario

    edades = [ [""+str(y)+"",edad.count(y)] for y in set(edad)]#generacion de array [edad,cantidad]

    edades = sorted(edades, key=lambda k: k[1], reverse=True) 

    #return HttpResponse(edades)
    return render_to_response("edt/edades.html",{"usuario" : usuarioObj,"edades":edades})    

                   
