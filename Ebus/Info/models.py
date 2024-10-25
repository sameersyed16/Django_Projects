from django.db import models
# Create your models here.
class businfo(models.Model):
    route=models.CharField(max_length=30)
    No=models.IntegerField()
