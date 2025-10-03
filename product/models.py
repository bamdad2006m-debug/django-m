from django.db import models

class task(models.Model):
    tital = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length=70)
    des = models.TextField()
    date = models.DateField()
    
