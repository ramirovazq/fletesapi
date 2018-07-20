from api.views import PhotoReactViewSet, LimeDemoViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'restphoto', PhotoReactViewSet, base_name='restphoto')
router.register(r'lime', LimeDemoViewSet, base_name='limedemo')

urlpatterns = router.urls
