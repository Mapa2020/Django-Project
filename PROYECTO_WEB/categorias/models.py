from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.timezone import timezone

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name ='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.name
      
class Producto(models.Model):
    titulo= models.CharField(max_length=50)
    imagen= models.ImageField(default='null', upload_to="productos")
    descripcion= models.CharField(max_length=100)
    precio= models.FloatField(default=0.0)
    categorias= models.ManyToManyField(Categoria, verbose_name="Categorias", blank=True, default="programa")
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name ='producto'
        verbose_name_plural='productos'
        ordering = ['-created']
    
    def __str__(self):
        return self.titulo
    
class Carrito(models.Model):
    usuario = models.CharField(max_length=50)
    lista_prod = models.CharField(max_length=100)
    total= models.FloatField(default=0.0)
    
    class Meta:
        verbose_name ='usuario'
        verbose_name_plural='usuarios'
    
    def __str__(self):
        return self.usuario
    