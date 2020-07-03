from rest_framework.serializers import ModelSerializer
from edt.models import *
class FuncionarioSerializer(ModelSerializer):


	class Meta:
		model =  Usuario
		fields = ('nombre', 'apellido1','apellido2')
