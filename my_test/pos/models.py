
# Create your models here.
from django.db import models

class Cliente(models.Model):
    puntos= models.DecimalField(max_digits=10,decimal_places=0)
    nombre= models.CharField(max_length=200)
    cedula= models.CharField(max_length=200)
    def __str__(self):
        return self.nombre+','+self.cedula+','+str(self.puntos)

class Carrito(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Factura(models.Model):
    costo= models.DecimalField(max_digits=10, decimal_places=4)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Producto(models.Model):
    nombre= models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=10,decimal_places=4)
    cantidad= models.DecimalField(max_digits=10,decimal_places=0, default='0')
    def __str__(self):
        return self.nombre
    def comprar(self):
        self.cantidad-=1
        return self


class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)






