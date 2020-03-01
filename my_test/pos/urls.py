
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.productoDetail, name='productoD'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:cliente_id>/',views.clienteDetail, name='clienteD'),
    path('facturas/', views.facturas, name='facturas'),
    path('facturas/<int:factura_id>/', views.facturaDetail, name='facturaD'),
    path('facturas/<int:factura_id>/productos/',views.productosFactura, name='productosF'), 
    path('carritos/',views.carritos, name='carritos' ), 
    path('carritos/<int:carrito>/productos/',views.productosCarrito, name='productosC' )
]