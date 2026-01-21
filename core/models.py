from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    marks = models.IntegerField()

    def __str__(self):
        return "f{self.roll}-{self.name}"
