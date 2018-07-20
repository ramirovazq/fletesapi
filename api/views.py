from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import PhotoReact, LimeDemo
from api.serializers import PhotoReactSerializer, LimeDemoSerializer

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
#from rest_framework.decorators import action
from django.conf import settings
from limesurveyrc2api.limesurvey import LimeSurvey

class PhotoReactViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = PhotoReact.objects.all()
    serializer_class = PhotoReactSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        serializer.save()


class LimeDemoViewSet(viewsets.ModelViewSet):

    queryset = LimeDemo.objects.none()
    serializer_class = LimeDemoSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        api_consulting = serializer.validated_data['api_consulting']
        email = serializer.validated_data['email']
        name = serializer.validated_data['name']

        token = ''
        if api_consulting == "YoffeCastanedaGattioniConsultores":
            url = settings.URL_API_LIME
            username = settings.USERNAME_API_LIME
            password = settings.PASSWD_API_LIME
            id_demo = settings.ID_DEMO_LIME

            # Open a session.
            api = LimeSurvey(url=url, username=username)
            api.open(password=password)
            respuesta = api.token.add_participants(id_demo, [{"email": email, "firstname": name}])
            try:
                dicc_respuesta = respuesta[0]
                token = dicc_respuesta['token']
            except IndexError:
                pass
            api.close()

        serializer.save(token=token)
