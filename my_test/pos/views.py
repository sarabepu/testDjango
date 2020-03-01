from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from pos.models import Carrito , Producto , Cliente, Factura, CarritoProducto


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def clienteDetail(request, cliente_id):
    
    p= Cliente.objects.get(pk=cliente_id)
    context={"client": p}
    return render(request,'pos/detail.html',context)

def productoDetail(request, producto_id):
    product = Producto.objects.get(pk=producto_id)
    context={"product": product}
    return render(request,'pos/detail.html',context)

def facturaDetail(request, factura_id):
    factura = Factura.objects.get(pk=factura_id)
    context={"factura": factura}
    return render(request,'pos/detail.html',context)

def productosCarrito(request,carrito):
    
    cp=CarritoProducto.objects.all().filter(carrito=carrito)
    
    context={'carrito':carrito,'productos_carrito': cp}
    return render(request,'pos/index.html', context)

def productosFactura(request,factura):
    fp=FacturaProducto.objects.all().filter(factura=factura)
    context={'factura':factura,'productos_factura': fp}
    return render(request,'pos/index.html', context)



def productos(request):
    products = Producto.objects.all()
    context={'products': products}
    return render(request,'pos/index.html', context)


def clientes(request):
    clients = Cliente.objects.all()
    context={'clients': clients}
    return render(request,'pos/index.html', context)

def carritos(request):
    carritos = Carrito.objects.all()
    context={'carritos': carritos}
    return render(request,'pos/index.html', context)


def facturas(request):
    facturas = Factura.objects.all()
    context={'facturas': facturas}
    return render(request,'pos/index.html', context)

