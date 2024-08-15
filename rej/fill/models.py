
from django.db import models

# Create your models here.
class tweet(models.Model):
    uname=models.CharField(max_length=30)
    post=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.uname