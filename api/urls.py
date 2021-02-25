from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'url', UrlViewSet)

urlpatterns = router.urls
