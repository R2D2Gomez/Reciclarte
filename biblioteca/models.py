from django.db import models

# Create your models here.

class rec_material  (models.Model):
    mat_elemento=models.CharField(max_length=250)
    mat_descripcion=models.CharField(max_length=2000)
    mat_video=models.CharField(max_length=500)
    mat_imagen=models.CharField(max_length=250)
    mat_url=models.CharField(max_length=250)

