# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.core.context_processors import csrf


class Rol (models.Model):
        nombre = models.CharField(max_length=32)
        nivel_acceso = models.IntegerField()
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre
class Cargo (models.Model):
        nombre = models.CharField(max_length=128)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Centrocosto (models.Model):
        nombre = models.CharField(max_length=32)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Estadoaprovacion (models.Model):
        nombre = models.CharField(max_length=32)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Estamento (models.Model):
        nombre = models.CharField(max_length=128)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Funcion (models.Model):
        nombre = models.CharField(max_length=128)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre            

class Jefatura (models.Model):
        nombre = models.CharField(max_length=128)
        correo1 = models.EmailField(max_length=128)
        correo2 = models.EmailField(max_length=128)
        correo3 = models.EmailField(max_length=128)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Nacionalidad (models.Model):
        nombre = models.CharField(max_length=32)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Contrato (models.Model):
        nombre = models.CharField(max_length=32)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre
            
class Sexo (models.Model):
        nombre = models.CharField(max_length=32)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Motivo (models.Model):
        nombre = models.CharField(max_length=100)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre

class Tipo_Permiso (models.Model):
        nombre = models.CharField(max_length=32)
        def __unicode__(self):              # __unicode__ on Python 2
            return self.nombre            

# Create your models here.
class Usuario(models.Model):
        rut = models.CharField(max_length=32)
        dv = models.CharField(max_length=1)
        nombre = models.CharField(max_length=32)
        apellido1 = models.CharField(max_length=32)
        apellido2 = models.CharField(max_length=32)
        funcion = models.ForeignKey(Funcion)
        rol= models.ForeignKey(Rol)
        cargo= models.ForeignKey(Cargo)
        estamento = models.ForeignKey(Estamento)
        jefatura = models.ForeignKey(Jefatura)
        username = models.CharField(max_length=32)
        password = models.CharField(max_length=32)
        correo = models.EmailField(max_length=128)
        horas_contratadas = models.CharField(max_length=32)
        fecha_nac = models.DateField()
        fecha_ingreso = models.DateField()
        sexo = models.ForeignKey(Sexo)
        telefono = models.CharField(max_length=32, null=True,blank=True)
        nacionalidad = models.ForeignKey(Nacionalidad)
        contrato = models.ForeignKey(Contrato)        
        foto = models.FileField(null=True,blank=True)

        class Meta:
            ordering = ('apellido1',)

        def __unicode__(self):              # __unicode__ on Python 2
            return "%s %s"%(self.apellido1,self.nombre)
devuelve = (
        ("S","SI"),
        ("N","NO")
)

goce = (
    ("C","Con goce de sueldo"),
    ("S","Sin goce de sueldo")

)

class Permiso (models.Model):
        usuario = models.ForeignKey(Usuario,null=True,blank=True)
        fecha_creacion = models.DateTimeField(auto_now_add=True,null=True,blank=True)
        horas_solicitadas = models.CharField(max_length=32,default=0)
        horas_solicitadas_funcionario = models.CharField(max_length=32,default=0,null=True,blank=True)        
        devuelve_horas = models.CharField(max_length=1,choices=devuelve)
        motivo = models.ForeignKey(Motivo,related_name="motivo")
        sueldo = models.CharField(max_length=1,choices=goce)
        reemplazante = models.ForeignKey(Usuario,related_name="reemplazante",null=True,blank=True,default=162)
        tipo = models.ForeignKey(Tipo_Permiso,related_name="tipo_permiso")
        comentario = models.CharField(max_length=500)
        documento_adjunto = models.FileField(null=True,blank=True)
        def __unicode__(self):              # __unicode__ on Python 2
                return u"%s el %s"%(self.usuario,self.fecha_creacion)

        def ultimaResolucion(self):
            if len(self.resolucion_set.all()) < 1:
                return None
            return self.resolucion_set.all().order_by('-id')[0]

        def ultimaBitacora(self):
            if len(self.bitacora_set.all()) < 1:
                return None
            return self.bitacora_set.all().order_by('-id')[0]

        def ultimoEvento(self):
            if len(self.eventos_en_permisos_set.all()) < 1:
                return None
            return self.eventos_en_permisos_set.all().order_by('-id')[0]

        def primerEvento(self):
            if len(self.eventos_en_permisos_set.all()) < 1:
                return None
            return self.eventos_en_permisos_set.all().order_by('id')[0]
        def horas(self):
            if len(self.horas_set.all()) < 1 :
                return None
            return self.horas_set.all()             
                                                                              


#esto no es una clase, solo una lista con listas inmutables (Tupla)
opciones = (
        ("A","Aprobado"),
        ("R","Rechazado"),
        ("N","Anulado")
)


class Foliocpe(models.Model):
    permiso = models.ForeignKey(Permiso)

class Folioprimaria(models.Model):
    permiso = models.ForeignKey(Permiso)

class Foliosecundaria(models.Model):
    permiso = models.ForeignKey(Permiso)   

class Foliogerencia(models.Model):
    permiso = models.ForeignKey(Permiso)

class Foliodirgen(models.Model):
    permiso = models.ForeignKey(Permiso)

class Foliomantencion(models.Model):
    permiso = models.ForeignKey(Permiso)

class Anulado(models.Model):
    permiso = models.ForeignKey(Permiso)
    anuladopor  = models.ForeignKey(Usuario)
    motivo = models.CharField(max_length=500, null=True)
    def __unicode__(self):
         return "permiso %s anulador por %s"%(self.permiso.id,self.anuladopor.nombre)


class Resolucion (models.Model):
        respuesta = models.CharField(max_length=1,choices=opciones)
        resolutor = models.ForeignKey(Usuario)
        razon = models.CharField(max_length=500, null=True)
        fecha_resolucion = models.DateField(auto_now_add=True)
        permiso = models.ForeignKey(Permiso)
        def __unicode__(self):              # __unicode__ on Python 2
            return "%s el %s"%(self.permiso.usuario,self.fecha_resolucion)

class Document(models.Model):
    usuario = models.ForeignKey(Usuario,null=True)
    filename = models.CharField(max_length=100)
    docfile = models.FileField() 
    def __unicode__(self):
            return "%s"%(self.docfile)           

class Evento (models.Model):
    usuario = models.ForeignKey(Usuario,related_name="edt_user")
    fecha_carga = models.DateTimeField(auto_now_add=True,null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    def __unicode__(self):
            return " %d"%(self.id)

class Eventos_en_Permisos(models.Model):
    numero_permiso = models.ForeignKey(Permiso)
    numero_evento = models.ForeignKey(Evento)
    deltainforme = models.CharField(max_length=32)
    deltafuncionario = models.CharField(max_length=32)
    #numero_permiso = models.CharField(max_length=32)
    #numero_evento = models.CharField(max_length=32) 
    def __unicode__(self):              # __unicode__ on Python 2
            return "%s  %s"%(self.numero_permiso,self.numero_evento)   
                
class Actividad(models.Model):
     nombre = models.CharField(max_length=32)
     def __unicode__(self):              # __unicode__ on Python 2
        return self.nombre

class Bitacora(models.Model):
    permiso = models.ForeignKey(Permiso,null=True) 
    usuario = models.ForeignKey(Usuario)
    actividad = models.ForeignKey(Actividad)
    fecha = models.DateTimeField(auto_now_add=True,null=True)
    def __unicode__(self):
        return "%s  %s"%(self.usuario,self.actividad)

class Horas(models.Model):
    permiso = models.ForeignKey(Permiso,null=True)
    fecha = models.DateTimeField(auto_now_add=True,null=True)
    usuario = models.ForeignKey(Usuario)
    horas_solicitadas = models.FloatField(default=0)
    horas_aprobadas = models.FloatField(default=0)
    horas_rechazadas = models.FloatField(default=0)
    horas_por_devolver = models.FloatField(default=0)
    horas_devueltas = models.FloatField(default=0)
    horas_descontar = models.FloatField(default=0)

    def __unicode__(self):
        return "%s %s"%(self.horas_solicitadas,self.permiso)

#######################################################################################################

class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(Usuario, blank=True, null=True)
    remind = models.BooleanField(default=False)

    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u" - " + self.title
        else:
            return unicode(self.creator) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return "<i>%s</i> - %s" % (self.title, self.snippet)
        else:
            return self.title
    short.allow_tags = True

    class Meta:
        verbose_name_plural = "entries"




