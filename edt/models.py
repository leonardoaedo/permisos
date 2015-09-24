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

        def __unicode__(self):              # __unicode__ on Python 2
            return "%s %s"%(self.nombre,self.apellido1)

devuelve = (
        ("S","SI"),
        ("N","NO")
)


class Permiso (models.Model):
        usuario = models.ForeignKey(Usuario,related_name="usuario")
        fecha_creacion = models.DateTimeField(auto_now_add=True)
        horas_solicitadas = models.CharField(max_length=32,default=0)
        devuelve_horas = models.CharField(max_length=1,choices=devuelve)
        reemplazante = models.ForeignKey(Usuario,related_name="reemplazante")
        documento_adjunto = models.FileField(null=True,blank=True)
        def __unicode__(self):              # __unicode__ on Python 2
                return "%s el %s"%(self.usuario,self.fecha_creacion)


#esto no es una clase, solo una lista con listas inmutables (Tupla)
opciones = (
        ("A","Aprobado"),
        ("R","Rechazado")
)


class Resolucion (models.Model):
        respuesta = models.CharField(max_length=1,choices=opciones)
        resolutor = models.ForeignKey(Usuario)
        razon = models.CharField(max_length=32, null=True,blank=True)
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
    delta = models.CharField(max_length=32)
    #numero_permiso = models.CharField(max_length=32)
    #numero_evento = models.CharField(max_length=32) 
    def __unicode__(self):              # __unicode__ on Python 2
            return "%s  %s"%(self.numero_permiso,self.numero_evento)   
                

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




