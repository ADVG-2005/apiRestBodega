from rest_framework.routers import DefaultRouter
from apps.registro.api.views import ViewSetRegistro

router_post_registro = DefaultRouter()
router_post_registro.register(prefix="registro",basename="registro",viewset=ViewSetRegistro)
