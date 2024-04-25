from django.db import models
# from django.utils import timezone

# Create your models here.


class Servo(models.Model):
    degree = models.CharField(max_length=3, default="")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.degree
