from django.db import models
# Create your models here.
class tweet(models.Model):
    uname=models.CharField(max_length=30)
    data=models.DateTimeField(auto_now_add=True)
    post=models.CharField(max_length=30)

    def __str__(self):
        return self(uname)
