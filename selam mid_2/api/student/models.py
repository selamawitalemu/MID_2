from django.db import models

# Create your models here.
class stud(models.Model):
    studname = models.CharField(max_length=30)
    Grade = models.IntegerField()
    Department = models.CharField( max_length=30)

    def __str__(self):
        return self.studname