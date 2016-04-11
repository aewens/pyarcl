from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ItemList(models.Model):
    creator = models.CharField(max_length=256)
    name = models.CharField(max_length=512)
    group = models.CharField(max_length=128)
    link = models.CharField(max_length=1024)

    def __str__(self):
        return self.creator + "@" + self.link

class Item(models.Model):
    item_list = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=16)
    file_name = models.CharField(max_length=256)
