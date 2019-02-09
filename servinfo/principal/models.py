from django.db import models

# Create your models here.
#cuando ejecutamos el comando en la consola para verificar la conexion con Mysql entonces
#este no arrojara un listado deacuerdo a como va en django las clases de nuestros modelos 
# el comando es el siguiente, python manage.py inspectdb.
class AccesoControl(models.Model):
    nit_acceso = models.CharField(primary_key=True, max_length=20)
    nombre_personal = models.CharField(max_length=20)
    apellido_personal = models.CharField(max_length=20)
    id_per = models.ForeignKey('Perfiles', models.DO_NOTHING, db_column='id_per')
    telefono = models.DecimalField(max_digits=10, decimal_places=0)
    foto = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acceso_control'
        unique_together = (('nit_acceso', 'id_per'),)


class Departamentos(models.Model):
    id_dep = models.AutoField(primary_key=True)
    nombre_dep = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Municipio(models.Model):
    id_muni = models.AutoField(primary_key=True)
    nombre_muni = models.CharField(max_length=20)
    id_dep = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_dep')

    class Meta:
        managed = False
        db_table = 'municipio'


class Perfiles(models.Model):
    id_per = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfiles'


class UsuariosVotos(models.Model):
    nit_user = models.CharField(primary_key=True, max_length=20)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    id_muni = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_muni')
    id_dep = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_dep')
    nit_acceso = models.ForeignKey(AccesoControl, models.DO_NOTHING, db_column='nit_acceso')
    fecha_registro = models.DateField()

    class Meta:
        managed = False
        db_table = 'usuarios_votos'




    


