from django.db import models

# Create your models here.

"""Aca creamos los modelos que queremos que tenga nuestra pagina
como por ejemplo, poder subir un post, un video, etc."""

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):
        return self.title # Esto es para que muestre el nombre del post y no el id que pone automaticamente