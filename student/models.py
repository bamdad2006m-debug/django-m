from django.db import models

class course(models.Model):
    title = models.CharField(max_length=64)
    code = models.PositiveIntegerField()
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.ManyToManyField()
    
    def __st__(self):
        return self.title
