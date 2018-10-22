from django.contrib import admin
from catalogo.models.categoria import Categoria
from catalogo.models_raiz import Producto
from catalogo.models_raiz import Venta
from catalogo.models_raiz import Detalle_venta
from catalogo.models_raiz import Cliente 
from catalogo.models_raiz import Empleado


# Register your models here.


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle_venta)
admin.site.register(Cliente)
admin.site.register(Empleado)