from django.db import models

# Create your models here.
class menu(models.Model):
    item=models.CharField(max_length=30)
    id=models.IntegerField()


    def __str__(self):
        return self.item
