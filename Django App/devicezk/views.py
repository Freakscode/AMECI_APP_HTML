from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import DeviceConnection

import subprocess

def biomconf(request):
    return render(request,'BiomConf.html')


def index(request):
    return render(request, 'index.html')


def connDev(request):
    result = subprocess.run(['python', 'AMECI_APP_HTML/Django App/connection.py'], capture_output = True)
    return HttpResponse(result.stdout)

def dev_detail(request, device_id):
    device = DeviceConnection.objects.get(id=1)
    return render(request, 'BiomConf.html', {'device': device})


def device_connection_data(request):
    latest_conn = get_object_or_404(DeviceConnection.objects.order_by('-id'))
    if latest_conn.conn:
        data = {
            'message': 'Conexión exitosa',
            'ip': latest_conn.ip,
            'port': latest_conn.port,
            'device_name': latest_conn.device_name,
            'firmware_version': latest_conn.firmware_version,
            'serial_number': latest_conn.serial_number,
        }
    else:
        data = {'message': 'No se encontró ninguna conexión'}
    return JsonResponse(data)
