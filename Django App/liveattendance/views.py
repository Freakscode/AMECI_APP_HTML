import datetime
from django.db.models import Max
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance, UsuariosActivos

def liveattendance(request):
    return render(request, 'liveattendance.html')


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def capture_attendance(request):
    active_users = UsuariosActivos.objects.all()

    for user in active_users:
        device_connection = user.device_connection
        Attendance.capture_attendance(device_connection)

    # Obtener los datos de asistencia y usuario para mostrar
    attendance_data = Attendance.objects.filter(
        timestamp__date=datetime.date.today()
    ).values(
        'user_id',
        'status'
    ).annotate(
        timestamp=Max('timestamp')
    )

    attendance_info = []
    for data in attendance_data:
        user_info = UsuariosActivos.objects.get(id=data['user_id'])
        attendance_info.append({
            'id': user_info.id,
            'nombre': user_info.nombre,
            'tarifa': user_info.tarifa,
            'status': data['status'],
            'timestamp': data['timestamp'],
        })

    # Devolver los datos en formato JSON
    return JsonResponse({'attendance_info': attendance_info})