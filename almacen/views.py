from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from almacen.utils import dame_token, dame_movimientos, agrega_picking, guardo_movimientos
from almacen.models import MovimientoAlmacen

from datetime import datetime
from pytz import timezone
import csv

@login_required
def sincroniza(request):
    
    context = {}
    context["resp_token"] = dame_token()
    token = context["resp_token"]["token"]
    movimientos = dame_movimientos(token)
    context["resp_movimientos"] = agrega_picking(movimientos, token)
    context["numero_nuevos"], context["numero_existia"]  = guardo_movimientos(context["resp_movimientos"])

    return render(request, 'almacen/index.html', context)

@login_required
def movimientos(request):
    
    context = {}

    movimientos = MovimientoAlmacen.objects.all()

    exporta = request.GET.get('exporta', False)

    if exporta in ["True", "true", "TRUE"]:
        exporta = True

    picking = request.GET.get('picking', False)
    producto = request.GET.get('producto', False)
    compania = request.GET.get('compania', False)
    propietario = request.GET.get('propietario', False)
    detalle = request.GET.get('detalle', '')


    fecha_creacion_inicio = request.GET.get('fecha_creacion_inicio', '')
    fecha_creacion_fin = request.GET.get('fecha_creacion_fin', '')

    ultima_actualizacion_inicio = request.GET.get('ultima_actualizacion_inicio', '')
    ultima_actualizacion_fin = request.GET.get('ultima_actualizacion_fin', '')

    fecha_programada_inicio = request.GET.get('fecha_programada_inicio', '')
    fecha_programada_fin = request.GET.get('fecha_programada_fin', '')


    if picking:
      movimientos = movimientos.filter(picking__icontains=picking)

    if producto:
      movimientos = movimientos.filter(picking__icontains=producto)

    if compania:
      movimientos = movimientos.filter(compania__icontains=compania)

    if propietario:
      movimientos = movimientos.filter(propietario__icontains=propietario)

    if detalle:
      movimientos = movimientos.filter(detalle__icontains=detalle)


    if fecha_creacion_inicio:
      movimientos = movimientos.filter(fecha_creacion__gte=datetime.strptime(fecha_creacion_inicio+'00:00:00', '%Y-%m-%d%H:%M:%S'))
    if fecha_creacion_fin:
      movimientos = movimientos.filter(fecha_creacion__lte=datetime.strptime(fecha_creacion_fin+'23:59:59', '%Y-%m-%d%H:%M:%S'))

    if ultima_actualizacion_inicio:
      movimientos = movimientos.filter(ultima_actualizacion__gte=datetime.strptime(ultima_actualizacion_inicio+'00:00:00', '%Y-%m-%d%H:%M:%S'))
    if ultima_actualizacion_fin:
      movimientos = movimientos.filter(ultima_actualizacion__lte=datetime.strptime(ultima_actualizacion_fin+'23:59:59', '%Y-%m-%d%H:%M:%S'))

    if fecha_programada_inicio:
      movimientos = movimientos.filter(fecha_programada__gte=datetime.strptime(fecha_programada_inicio+'00:00:00', '%Y-%m-%d%H:%M:%S'))
    if fecha_programada_fin:
      movimientos = movimientos.filter(fecha_programada__lte=datetime.strptime(fecha_programada_fin+'23:59:59', '%Y-%m-%d%H:%M:%S'))




    if exporta == True:
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)
        writer.writerow(['Picking', 'Producto', 'Cantidad', 'Tractor o Compañía', \
                         'Propietario', 'Detalle',\
                         'Fecha Creacion', 'Ultima Actualizacion', 'Fecha Programada', \
                         'De', 'Para','estado'])
        for movimiento in movimientos:
              renglon = []
              renglon.append(movimiento.picking)
              renglon.append(movimiento.producto) 
              renglon.append(movimiento.cantidad) 
              renglon.append(movimiento.compania) 
              renglon.append(movimiento.propietario)
              renglon.append(movimiento.detalle)

              if movimiento.fecha_creacion:                
                renglon.append(movimiento.fecha_creacion.astimezone(timezone(settings.TIME_ZONE)).strftime("%Y-%m-%d %H:%M"))
              if movimiento.ultima_actualizacion:
                renglon.append(movimiento.ultima_actualizacion.astimezone(timezone(settings.TIME_ZONE)).strftime("%Y-%m-%d %H:%M"))
              if movimiento.fecha_programada:
                renglon.append(movimiento.fecha_programada.astimezone(timezone(settings.TIME_ZONE)).strftime("%Y-%m-%d %H:%M"))

              renglon.append(movimiento.de)
              renglon.append(movimiento.para)
              renglon.append(movimiento.estado)       
              writer.writerow(renglon)
        return response

    context["movimientos"] = movimientos
    return render(request, 'almacen/movimientos.html', context)