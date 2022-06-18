from mailbox import NoSuchMailboxError
from turtle import update
from django.db import models


# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="CategoriasProd"
        #devuelve nombre de categoria
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) 
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True) 
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"