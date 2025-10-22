from django.db import models

class task(models.Model):
    tital = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length=70)
    des = models.TextField()
    date = models.DateField()
    student = models.ForeignKey(student,on_delete=models.CASCADE,related_name="task")
    def __st__(self):
        return self.title
