from django.contrib import admin

# Register your models here.

from pos.models import Carrito , Producto , Cliente, Factura, CarritoProducto

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)

admin.site.register(Factura)