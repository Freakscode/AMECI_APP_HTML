from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Lower
from .models import UsuariosActivos


def index(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'users.html')


def usuarios_activos(request):
    usuarios = UsuariosActivos.objects.order_by('fechavencimiento')
    usuarios_serialized = serializers.serialize('json', usuarios, fields=('nombre', 'cedula', 'celular', 'tarifa', 'fechainicio', 'fechavencimiento', 'id'), use_natural_primary_keys=True)
    return JsonResponse(usuarios_serialized, safe=False)