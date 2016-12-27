from edt.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from django.db.models import Count, Min, Sum, Avg , F

def procesa_resolucion(request,id,usuarioObj): # procesa resolucion, guarda en Bitacora y enviar email
	
	actividad = id	
	resu = Resolucion()
	resu.respuesta = request.POST['respuesta']
	resu.resolutor = Usuario.objects.get(id=request.session['usuario'])
	resu.razon = request.POST['razon']
	resu.permiso = Permiso.objects.get(id=request.POST['permiso'])
	resu.save()
	bitacora = Bitacora(actividad=actividad,usuario=usuarioObj,permiso=resu.permiso)
	bitacora.save()
	gerente = Funcion.objects.get(nombre='Gerente')

	if resu.resolutor.funcion == gerente or resu.respuesta == 'R':
		#email solicitante, solo en la ultima revision que es efectuada por el Gerente
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {
											'nombre' : resu.permiso.usuario.nombre,
											'apellido' : resu.permiso.usuario.apellido1,
											'horas':resu.permiso.horas_solicitadas,
											'permiso':resu.permiso.id,
											'respuesta' : resu.get_respuesta_display})
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
 

 	resolucion = Resolucion.objects.annotate(contar=Count('permiso')).filter(permiso=resu.permiso)

	if resu.permiso.usuario.jefatura == administracion and resolucion[0].contar == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()

	if resu.permiso.usuario.jefatura == administracion and resolucion[0].contar == 2:
		#email a jefatura en Segunda Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()

	if resu.permiso.usuario.jefatura == primaria and resolucion[0].contar == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 

	if resu.permiso.usuario.jefatura == primaria and resolucion[0].contar == 2:
		#email a jefatura en Segunda Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()

	if resu.permiso.usuario.jefatura == primaria and resolucion[0].contar == 3:
		#email a jefatura en Tercera Revision
	    template = loader.get_template('edt/email_respuesta.html')
	    context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,'apellido' : resu.permiso.usuario.apellido1,'horas':resu.permiso.horas_solicitadas,'permiso':resu.permiso.id,'respuesta' : resu.get_respuesta_display})
	    html = template.render(context)
	    msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 
	    
	if resu.permiso.usuario.jefatura == secundaria and resolucion[0].contar == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 

	if resu.permiso.usuario.jefatura == secundaria and resolucion[0].contar == 2:
		#email a jefatura en Segunda Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()

	if resu.permiso.usuario.jefatura == secundaria and resolucion[0].contar == 3:
	# 	#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':resu.permiso.id,
										   'respuesta' : resu.get_respuesta_display})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send() 

	if resu.permiso.usuario.jefatura == servicio and resolucion[0].contar == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 

	if resu.permiso.usuario.jefatura == servicio and resolucion[0].contar == 2:
		#email a jefatura en Segunda Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()

	if resu.permiso.usuario.jefatura == servicio and resolucion[0].contar == 3:
		#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':resu.permiso.id,
										   'respuesta' : resu.get_respuesta_display})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send() 

	if resu.permiso.usuario.jefatura == viesco and resolucion[0].contar == 1:
		#email a jefatura en Primera Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo2])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send() 

	if resu.permiso.usuario.jefatura == viesco and resolucion[0].contar == 2:
		#email a jefatura en Segunda Revision
	    template = loader.get_template('edt/email_jefatura.html')
	    context = RequestContext(request, {'jefe' : resu.permiso.usuario.jefatura.nombre,
	    								   'horas':resu.permiso.horas_solicitadas,
	    								   'numero':resu.permiso.id,
	    								   'nombre' : resu.permiso.usuario.nombre,
	    								   'apellido' : resu.permiso.usuario.apellido1,
	    								   'rut': resu.permiso.usuario.rut,
	    								   'dv':resu.permiso.usuario.dv,
	    								   'nom_reemplazante':resu.permiso.reemplazante.nombre,
	    								   'ap_reemplazante':resu.permiso.reemplazante.apellido1,
	    								   'fecha': resu.permiso.fecha_creacion})
	    html = template.render(context)
	    msg = EmailMessage('Solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.jefatura.correo3])
	    msg.content_subtype = "html"  # Main content is now text/html
	    msg.send()

	if resu.permiso.usuario.jefatura == viesco and resolucion[0].contar == 3:
		#email a jefatura en Tercera Revision
		template = loader.get_template('edt/email_respuesta.html')
		context = RequestContext(request, {'nombre' : resu.permiso.usuario.nombre,
										   'apellido' : resu.permiso.usuario.apellido1,
										   'horas':resu.permiso.horas_solicitadas,
										   'permiso':resu.permiso.id,
										   'respuesta' : resu.get_respuesta_display})
		html = template.render(context)
		msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [resu.permiso.usuario.correo])
		msg.content_subtype = "html"  # Main content is now text/html
		msg.send()     
	return (resu)