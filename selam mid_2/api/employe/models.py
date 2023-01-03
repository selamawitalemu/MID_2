from django.db import models

# Create your models here.
class emplo(models.Model):
    emploname = models.CharField(max_length=30)
    salary = models.IntegerField()
    Department = models.CharField( max_length=30)

    def __str__(self):
        return self.emploname