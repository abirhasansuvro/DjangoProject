from django.db import models

class SBO(models.Model):
    name= models.CharField(max_length=50, null=True, blank=False)
    location= models.CharField(max_length=200, null=True, blank=False)
    no_of_employees= models.IntegerField(null=True, blank=False)
    area_square_ft= models.FloatField(null=True, blank=False)
    is_shop = models.BooleanField(default=False)
    is_branch = models.BooleanField(default=False)
    is_outlet = models.BooleanField(default=False)

    def __str__(self):
        return self.name
