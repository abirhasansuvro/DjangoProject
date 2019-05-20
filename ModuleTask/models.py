from django.db import models

# Create your models here.
class Modules(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=20)
    order=models.IntegerField()

    def __str__(self):
        return self.name+self.code
