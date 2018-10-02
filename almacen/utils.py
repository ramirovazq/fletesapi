import requests
from django.conf import settings

def dame_token():
  context = {}
  url = settings.URL_BASE_API + settings.URL_API_AUTHENTICATE
  response = requests.post(url, data={'db':settings.CONNECT_DB, 'login':settings.CONNECT_LOGIN, 'password':settings.CONNECT_PASSWORD})

  if response.ok:
    print("request OK ...")
    response_json = response.json()
    try:
      context['token'] = response_json["token"]
    except KeyError:
      context['token'] = None
  else:
    print("error en request")

  #print(context)
  return context


def dame_movimientos(token):
  context = {}
  url = settings.URL_BASE_API + "/read/stock.move.line/"
  response = requests.post(url, data={'token':token})

  if response.ok:
    print("request OK ...")
    response_json = response.json()
    try:
      context['movimientos'] = response_json
    except KeyError:
      context['movimientos'] = None
  else:
    print("error en request")

  #print(context)
  return context


def dame_picking(picking_id, token):
  url = settings.URL_BASE_API + "/read/stock.picking/{}".format(picking_id)
  response = requests.post(url, data={'token':token})
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
