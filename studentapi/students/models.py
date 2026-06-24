from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolment_date = models.DateField
    grade_level = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    is_active = models.BooleanField(default=True)