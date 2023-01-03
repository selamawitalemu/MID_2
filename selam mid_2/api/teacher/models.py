from django.db import models

# Create your models here.
class teac(models.Model):
    teacname = models.CharField(max_length=30)
    salary = models.IntegerField()
    Department = models.CharField( max_length=30)

    def __str__(self):
        return self.teacname