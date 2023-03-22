from django.db import models

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
class Videos(models.Model):
    titulo = models.CharField(max_length=200)
    idvideo = models.CharField(max_length=200)