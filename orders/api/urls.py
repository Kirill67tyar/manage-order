from django import urls
from rest_framework.routers import DefaultRouter

from orders.api.views import (
    ColorCarModelViewSet,
    MarkCarModelViewSet,
    ModelCarModelViewSet,
    OrderModelViewSet,
)

app_name = 'api'

# urlpatterns = [
#
# ]
router = DefaultRouter()
router.register(
    prefix='colors',
    viewset=ColorCarModelViewSet,
    basename='colors'
)
router.register(
    prefix='marks',
    viewset=MarkCarModelViewSet,
    basename='marks'
)
router.register(
    prefix='models',
    viewset=ModelCarModelViewSet,
    basename='models'
)
router.register(
    prefix='orders',
    viewset=OrderModelViewSet,
    basename='orders'
)

urlpatterns = router.urls
