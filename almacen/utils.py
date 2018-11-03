from datetime import datetime
from django.conf import settings
from .models import MovimientoAlmacen
import requests

def dame_token():
  context = {}
  url = settings.URL_BASE_API + settings.URL_API_AUTHENTICATE
  response = requests.post(url, data={'db':settings.CONNECT_DB, 'login':settings.CONNECT_LOGIN, 'password':settings.CONNECT_PASSWORD})

  if response.ok:
    response_json = response.json()
    try:
      context['token'] = response_json["token"]
    except KeyError:
      context['token'] = None
  else:
    print("error en request...1")
    print(response.text)

  #print(context)
  return context


def dame_movimientos(token):
  context = {}
  url = settings.URL_BASE_API + "/read/stock.move.line/"
  response = requests.post(url, data={'db':settings.CONNECT_DB,'token':token})

  if response.ok:
    response_json = response.json()
    try:
      context['movimientos'] = response_json
    except KeyError:
      context['movimientos'] = None
  else:
    print("error en request...2")
    print(response.text)

  #print(context)
  return context


def dame_picking(picking_id, token):
  url = settings.URL_BASE_API + "/read/stock.picking/{}".format(picking_id)
  response = requests.post(url, data={'db':settings.CONNECT_DB,'token':token})
  if response.ok:
    return response.json()
  else:
    return response


def dame_product(product_id, token):
  url = settings.URL_BASE_API + "/read/product.template/{}".format(product_id)
  response = requests.post(url, data={'db':settings.CONNECT_DB,'token':token})
  if response.ok:
    return response.json()
  else:
    return response



def agrega_picking(diccionario, token):
  diccionario_new = {"movimientos": []}
  if 'movimientos' in diccionario.keys():
    for x in diccionario['movimientos']:
      if x['picking_id']:
        picking_id_post = x['picking_id'][0]
        response_json = dame_picking(picking_id_post, token)
        x['response_picking'] = response_json
        #print("--------------------------INI")
        #print(x)
        #print("--------------------------FIN")
        diccionario_new['movimientos'].append(x)

      else:
        #print("--------------------------INI----////////")
        #print(x)
        #print("--------------------------FIN----////////")
        diccionario_new['movimientos'].append(x)
  return diccionario_new 


def agrega_detalle_producto(diccionario, token):
  diccionario_new = {"producto_detalle": []}
  if 'movimientos' in diccionario.keys():
    for x in diccionario['movimientos']:
      if x['product_id']:
        product_id_post = x['product_id'][0]
        response_json = dame_product(product_id_post, token)
        x['response_product_detail'] = response_json
        diccionario_new['producto_detalle'].append(x)

      else:
        diccionario_new['producto_detalle'].append(x)
  return diccionario_new 



def guardo_movimientos(diccionario, diccionariodos):
  contador_nuevo = 0
  contador_existia = 0
  for movimiento, productodetalle in zip(diccionario['movimientos'], diccionariodos['producto_detalle']):

    print("----")
    print(movimiento['id'] == productodetalle['id'])

    dicc_default = {
      "id_api": movimiento['id'],
      "fecha_creacion": datetime.strptime(movimiento['create_date'] + '+0000', '%Y-%m-%d %H:%M:%S%z'),##+5 es el buenos
      #"fecha_programada": datetime.strptime(movimiento['write_date'], '%Y-%m-%d %H:%M:%S'),
      #"fecha_hecho": datetime.strptime(movimiento['write_date'], '%Y-%m-%d %H:%M:%S'),
      "ultima_actualizacion": datetime.strptime(movimiento["write_date"]+ '+0000', '%Y-%m-%d %H:%M:%S%z'),
      #"picking": movimiento["picking_id"][1],
      "cantidad": movimiento["qty_done"],
      "producto": movimiento["display_name"],
      #"de": de,
      #"para": para, 
      "estado":  movimiento["state"],
      #"compania": movimiento['response_picking'][0]['partner_id'][1]
      #"detalle": movimiento['']
    }

    if productodetalle["response_product_detail"]:
      dicc_default["precio_costo_unitario"] = productodetalle["response_product_detail"][0]["standard_price"]
      dicc_default["precio_venta_unitario"] = productodetalle["response_product_detail"][0]["list_price"]
      dicc_default["precio_costo_total"] = productodetalle["response_product_detail"][0]["standard_price"] * movimiento["qty_done"]

    if movimiento["picking_id"]:
      dicc_default["picking"]= movimiento["picking_id"][1]

    if 'response_picking' in movimiento.keys():
      dicc_default['de'] = movimiento['response_picking'][0]['location_id'][1]
    else:
      dicc_default['de'] = movimiento['location_id'][1] 

    if 'response_picking' in movimiento.keys():
      dicc_default['para'] = movimiento['response_picking'][0]['location_dest_id'][1] 
    else:
      dicc_default['para'] = movimiento['location_dest_id'][1] 

    if 'response_picking' in movimiento.keys():
      if movimiento['response_picking'][0]['owner_id']: #movimiento.response_picking.0.owner_id.1
        dicc_default["propietario"] = movimiento['response_picking'][0]['owner_id'][1]
      if movimiento['owner_id']:
        dicc_default["detalle"] = movimiento['owner_id'][1]
    else:
      dicc_default["propietario"] = movimiento['owner_id']


    if 'response_picking' in movimiento.keys():

      if movimiento['response_picking'][0]['scheduled_date']:
        dicc_default['fecha_programada'] = datetime.strptime(movimiento['response_picking'][0]['scheduled_date'] + '+0000', '%Y-%m-%d %H:%M:%S%z')

      if movimiento['response_picking'][0]['date_done']:
        dicc_default['fecha_hecho'] = datetime.strptime(movimiento['response_picking'][0]['date_done'] + '+0000', '%Y-%m-%d %H:%M:%S%z')

      if movimiento['response_picking'][0]['partner_id']:
        dicc_default["compania"] = movimiento['response_picking'][0]['partner_id'][1]





    objeto, es_nuevo = MovimientoAlmacen.objects.get_or_create(id_api=movimiento['id'], defaults=dicc_default)
    if es_nuevo:
      contador_nuevo = contador_nuevo + 1
    else:
      contador_existia = contador_existia + 1

  return contador_nuevo, contador_existia

