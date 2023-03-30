from django.db import models
from zk import ZK, const

class DeviceConnection ( models.Model ) :
    ip = models.CharField ( max_length = 20 )
    port = models.CharField ( max_length = 5 )
    conn = models.BooleanField ( default = False )
    device_name = models.CharField ( max_length = 50 , null = True , blank = True )
    firmware_version = models.CharField ( max_length = 100 , null = True , blank = True )
    serial_number = models.CharField ( max_length = 500 , null = True , blank = True )

    def __str__ ( self ) :
        return self.ip

    def save ( self , *args , **kwargs ) :
        zk = ZK ( self.ip , self.port )
        conn_dev = zk.connect ( )

        try :
            existing_conn = DeviceConnection.objects.get ( ip = self.ip , port = self.port )
        except DeviceConnection.DoesNotExist :
            existing_conn = None

        if conn_dev :
            if existing_conn :
                existing_conn.conn = True
                existing_conn.device_name = zk.get_device_name ( )
                existing_conn.firmware_version = zk.get_firmware_version ( )
                existing_conn.serial_number = zk.get_serialnumber ( )
                existing_conn.save ( )
            else :
                self.conn = True
                self.device_name = zk.get_device_name ( )
                self.firmware_version = zk.get_firmware_version ( )
                self.serial_number = zk.get_serialnumber ( )
                super ( ).save ( *args , **kwargs )
        else :
            if existing_conn :
                existing_conn.conn = False
                existing_conn.device_name = None
                existing_conn.firmware_version = None
                existing_conn.serial_number = None
                existing_conn.save ( )
            else :
                self.conn = False
                self.device_name = None
                self.firmware_version = None
                self.serial_number = None
                super ( ).save ( *args , **kwargs )

    class Meta :
        db_table = 'device_connection_at'

class Attendance(models.Model):
    device_connection = models.ForeignKey(DeviceConnection, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'attendance'

    @classmethod
    def capture_attendance(cls, device_connection):
        zk = ZK(device_connection.ip, device_connection.port)
        conn = zk.connect()
        try:
            for attendance in conn.live_capture():
                if attendance is not None:
                    cls.objects.create(
                        device_connection=device_connection,
                        timestamp=attendance.timestamp,
                        user_id=attendance.user_id,
                        status=attendance.status
                    )
        finally:
            conn.disconnect()

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
        db_table = 'usuariosactivos_at'