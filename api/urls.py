from api.views import PhotoReactViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'restphoto', PhotoReactViewSet, base_name='restphoto')

urlpatterns = router.urls
