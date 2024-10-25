from django.db import models
# Create your models here.
class insta(models.Model):
    person=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    caption=models.CharField(max_length=300)
    pic=models.ImageField(upload_to='media')
    def __str__(self):
        return self.caption