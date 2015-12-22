from edt.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template import RequestContext, loader
from django.template.loader import render_to_string

def procesa_resolucion(request,id,usuarioObj): # procesa resolucion, guarda en vitacora y enviar email
	
	actividad = id	
	resu = Resolucion()
	resu.respuesta = request.POST['respuesta']
	resu.resolutor = Usuario.objects.get(id=request.session['usuario'])
	resu.razon = request.POST['razon']
	resu.permiso = Permiso.objects.get(id=request.POST['permiso'])
	resu.save()
	bitacora = Bitacora(actividad=actividad,usuario=usuarioObj,permiso=resu.permiso)
	bitacora.save()
	template = loader.get_template('edt/email_respuesta.html')
	context = RequestContext(request, {'nombre' : usuarioObj.nombre,'apellido' : usuarioObj.apellido1,'horas':resu.permiso.horas_solicitadas,'permiso':resu.permiso.id,'respuesta' : resu.respuesta})
	html = template.render(context)
	msg = EmailMessage('Respuesta a solicitud de permiso', html, 'scpa@cdegaulle.cl', [usuarioObj.correo])
	msg.content_subtype = "html"  # Main content is now text/html
	msg.send()

	return (resu)