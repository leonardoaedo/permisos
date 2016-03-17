# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from edt.models import *

class PermisoFormSet(forms.ModelForm):
    class Meta:
       model = Permiso
  
       exclude = ["usuario","horas_solicitadas","horas_solicitadas_funcionario"]
        

class PermisoFormSetEdit(forms.ModelForm):
    class Meta:
       model = Permiso
       exclude = ["usuario","horas_solicitadas","horas_solicitadas_funcionario","motivo","tipo","reemplazante","documento_adjunto"]       

    
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