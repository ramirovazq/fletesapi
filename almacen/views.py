from django.http import HttpResponse
from django.shortcuts import render
from almacen.utils import dame_token, dame_movimientos, agrega_picking, guardo_movimientos
from almacen.models import MovimientoAlmacen
from datetime import datetime

def sincroniza(request):
    
    context = {}
    context["resp_token"] = dame_token()
    token = context["resp_token"]["token"]
    movimientos = dame_movimientos(token)
    context["resp_movimientos"] = agrega_picking(movimientos, token)
    context["numero_nuevos"], context["numero_existia"]  = guardo_movimientos(context["resp_movimientos"])

    return render(request, 'almacen/index.html', context)

def movimientos(request):
    
    context = {}

    movimientos = MovimientoAlmacen.objects.all()

    fecha_programada_inicio = request.GET.get('fecha_programada_inicio', '')
    fecha_programada_fin = request.GET.get('fecha_programada_fin', '')
    compania = request.GET.get('compania', '')
    propietario = request.GET.get('propietario', '')
    detalle = request.GET.get('detalle', '')

    if fecha_programada_inicio:
      movimientos = movimientos.filter(fecha_programada__gte=datetime.strptime(fecha_programada_inicio+'00:00:00', '%Y-%m-%d%H:%M:%S'))
    if fecha_programada_fin:
      movimientos = movimientos.filter(fecha_programada__lte=datetime.strptime(fecha_programada_fin+'23:59:59', '%Y-%m-%d%H:%M:%S'))
    if compania:
      movimientos = movimientos.filter(compania__icontains=compania)
    if propietario:
      movimientos = movimientos.filter(propietario__icontains=propietario)
    if detalle:
      movimientos = movimientos.filter(detalle__icontains=detalle)



    context["movimientos"] = movimientos
    return render(request, 'almacen/movimientos.html', context)