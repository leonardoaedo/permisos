# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from edt.models import *
from django import forms

class LicenciaFormset(forms.ModelForm):
  class Meta:
    model = Licencia
    exclude = ["inicio","fin","horas","ingresadopor"]


class PermisoFormSet(forms.ModelForm):
    class Meta:
       model = Permiso
  
       exclude = ["usuario","horas_solicitadas","horas_solicitadas_funcionario","estado"]
        

class PermisoFormSetEdit(forms.ModelForm):
    class Meta:
       model = Permiso
       exclude = ["usuario","horas_solicitadas","horas_solicitadas_funcionario","motivo","tipo","reemplazante","documento_adjunto","estado"]       

    
class ResolucionFormSet(forms.ModelForm):
        class Meta:
           model = Resolucion
           exclude = [""]

        
class HorasFormSet(forms.ModelForm):
    class Meta:
        model = Horas
        exclude = ["horas_solicitadas","permiso"]


class DocumentFormSet(forms.ModelForm):
        class Meta:
           model = Document
           exclude = [""]

class FormacionForm(forms.ModelForm):
        class Meta :
            model = Formacion
            exclude =[""]

class SalidaPedagogicaForm (forms.ModelForm):
    class Meta:
        model = SalidaPedagogica
        exclude = [""]


