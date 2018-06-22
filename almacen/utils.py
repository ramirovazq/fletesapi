import requests
from django.conf import settings

def dame_token():
  context = {}
  url = settings.URL_API_AUTHENTICATE
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

  print(context)
  return context