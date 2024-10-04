from rest_framework.routers import DefaultRouter
from apps.salida.api.views import SalidaViewSet

router_post = DefaultRouter()

router_post.register(prefix="salida",basename="salida",viewset=SalidaViewSet)