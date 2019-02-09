#Llamamos los modelos creados anteriromente
from .models import AccesoControl, Departamentos, Municipio, MesaJurado, Perfiles, UsuariosVotos
#llamamos el rest framework indicado en la configuracion
from rest_frameork import serializers

#creamos las lcases como por ejemplo de un formulario
 class AccesoControlSerialize(serializers.ModelSerializer):
 	class Meta:
 			model-Accesocontrol
 			fields-('nit_acceso','nombre_personal','apellido_personal','id_per','telefono','foto')

class DepartamentosSerialize(serializers.ModelSerializer):
 	class Meta:
 			model-Departamentos
 			fields-('id_dep','nombre_dep')

class MesajuradoSerialize(serializers.ModelSerializer):
 	class Meta:
 			model-Mesa
 			fields-('id_mesa','nombre_mesa')
 			
class MunicipioSerialize(serializers.ModelSerializer):
 	class Meta:
 			model-Municipio
 			fields-('id_muni','nombre_muni')

class PerfilesSerialize(serializers.ModelSerializer):
 	class Meta:
 			model-Perfiles
 			fields-('id_per','nombre_rol')

