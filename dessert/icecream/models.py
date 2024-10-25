from django.db import models

# Create your models here.
class menu(models.Model):
    brand=models.CharField(max_length=30)
    flavour=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.brand
