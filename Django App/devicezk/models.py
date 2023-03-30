from django.db import models
import os , sys
from zk import ZK

CWD = os.path.dirname ( os.path.realpath ( __file__ ) )
ROOT_DIR = os.path.dirname ( CWD )
sys.path.append ( ROOT_DIR )


# Create your models here.
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
        db_table = 'device_connection'
