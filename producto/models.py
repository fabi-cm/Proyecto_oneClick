from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre Categoria')
    img = models.ImageField(default='categorias/img_defecto.jpg', upload_to='categorias/', verbose_name='Imagen de categoria')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
    
    def __str__(self):
        return "{0}".format(self.nombre)

class Productos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='producto')
    nombre = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nombre de producto')
    img = models.ImageField(default='productos/img_defecto.jpg', upload_to='productos/', verbose_name='Imagen de producto')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name='Categorias', null=True, blank=True)
    descripcion = models.TextField(max_length=500, null=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-id']

    def __str__(self):
        return "Producto: {0} , Categorias: {1}".format(self.nombre, self.categoria)
    
