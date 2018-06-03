from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import PhotoReact
from api.serializers import PhotoReactSerializer

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
#from rest_framework.decorators import action


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
