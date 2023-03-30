from django.db import models

class UsuariosActivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    tarifa = models.CharField ( max_length = 50 )
    cedula = models.CharField(max_length=50)
    fechainicio = models.DateField()
    fechavencimiento = models.DateField()
    diasrestantes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuariosactivos'
