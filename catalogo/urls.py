
from django.conf.urls import url, include
from rest_framework import routers
from .views.categoria_view import CategoriaViewSet
from .views.cliente_view import ClienteViewSet
from .views.detalle_venta_view import Detalle_ventaViewSet
from .views.empleado_view import EmpleadoViewSet
from .views.producto_view import ProductoViewSet
from .views.venta_view import VentaViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'detalle_ventas', Detalle_ventaViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
