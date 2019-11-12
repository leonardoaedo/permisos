from edt.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from django.db.models import Count, Min, Sum, Avg , F

def procesa_modificacion(request,id,usuarioObj): # procesa modificacion, guarda en Bitacora y enviar email
	actividad = id
	resu = Resolucion()
	resu.respuesta = request.POST['respuesta']
	resu.resolutor = Usuario.objects.get(id=request.session['usuario'])
	resu.razon = request.POST['comentario']
	resu.permiso = Permiso.objects.get(id=request.POST['permiso'])
	aut = request.POST['autorizador']
	autorizador = Usuario.objects.get(id=aut)
	permiso = Permiso.objects.get(id=request.POST['permiso'])
	resu.save()
	bitacora = Bitacora(autorizador=autorizador,actividad=actividad,usuario=usuarioObj,permiso=resu.permiso,comentario=resu.razon)
	bitacora.save()
	resolucion = Resolucion.objects.annotate(contar=Count('permiso')).filter(permiso=resu.permiso)

	contador = 0
	for r in resolucion:
		contador = 1 + contador
		print contador
	
	if resu.respuesta == 'M':
		#email a usuario, comprobante de modificacion
		template = loader.get_template('edt/email_modificacion.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'autorizador' : autorizador,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Modificacion de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send()

		#email a jefatura en modificacion
		template = loader.get_template('edt/email_jefatura_modificacion.html')
		context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
										   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'comentario' : resu.razon,
	    								   'autorizador' : autorizador,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Modificacion de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send()  	

	return (resu)	

def procesa_resolucion(request,id,usuarioObj): # procesa resolucion, guarda en Bitacora y enviar email
	
	actividad = id	
	resu = Resolucion()
	resu.respuesta = request.POST['respuesta']
	resu.resolutor = Usuario.objects.get(id=request.session['usuario'])
	resu.razon = request.POST['razon']
	resu.permiso = Permiso.objects.get(id=request.POST['permiso'])
	permiso = Permiso.objects.get(id=request.POST['permiso'])
	resu.save()
	bitacora = Bitacora(actividad=actividad,usuario=usuarioObj,permiso=resu.permiso)
	bitacora.save()

	gerente = Funcion.objects.get(nombre='Gerente')
	resolucion = Resolucion.objects.annotate(contar=Count('permiso')).filter(permiso=resu.permiso)
	contador = 0
	for r in resolucion:
		contador = 1 + contador
		print contador
	

	
	if resu.resolutor.funcion == gerente or resu.respuesta == 'R':
		#email solicitante, solo en la ultima revision que es efectuada por el Gerente
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send()

 	administracion = Jefatura.objects.get(nombre='Gerencia')
 	primaria = Jefatura.objects.get(nombre='Direccion Primaria')
 	secundaria = Jefatura.objects.get(nombre='Direccion Secundaria')
 	prim_secund = Jefatura.objects.get(nombre='Primaria-Secundaria')
 	servicio = Jefatura.objects.get(nombre='Mantencion y aseo')
 	viesco = Jefatura.objects.get(nombre='CPE')
 	test = Jefatura.objects.get(nombre='Test')
 
	if resu.permiso.usuario.jefatura == primaria and contador == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 

	if resu.permiso.usuario.jefatura == administracion and contador >= 1:
		#email a jefatura en Segunda Revision
	    template = loader.get_template('edt/email_respuesta.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()


	if resu.permiso.usuario.jefatura == primaria and contador >= 2:
		#email a jefatura en Tercera Revision
	    template = loader.get_template('edt/email_respuesta.html')
	    context = RequestContext(request,{'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 
	    
	if resu.permiso.usuario.jefatura == secundaria and contador == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 


	if resu.permiso.usuario.jefatura == secundaria and contador >= 2:
	# 	#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send() 

	if resu.permiso.usuario.jefatura == servicio and contador == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 

	if resu.permiso.usuario.jefatura == servicio and contador >= 2:
		#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send() 

	if resu.permiso.usuario.jefatura == viesco and contador == 1 :
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 


	if resu.permiso.usuario.jefatura == viesco and contador >= 2:
		#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send()
		
	
############################################ envio de correos TEST##############################################
		
	if resu.permiso.usuario.jefatura.id == 8 and contador == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'permiso':permiso,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion,
	    								   'resolucion' : resolucion[contador-1]})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 


	if resu.permiso.usuario.jefatura.id == 8 and contador >= 2:
		#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':permiso,
										   'respuesta' : resu.get_respuesta_display,
	    								   'resolucion' : resolucion[contador-1]})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send()	     
############################################ envio de correos TEST##############################################


	return (resu)