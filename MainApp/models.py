from django.db import models

# Create your models here.

class Item(models.Model):
   name  = models.CharField('Название', max_length=100)
   brand = models.CharField('Бренд', max_length=100)
   count = models.PositiveIntegerField('Количество') 
   description = models.TextField('Описание', blank=True)