from django.db import models
from RoleCreation.models import Roles

# Create your models here.

class UserWithRole(models.Model):
    role=models.ManyToManyField(Roles)
    UserName=models.CharField(max_length=50)
    DisplayName=models.CharField(max_length=40)
    email=models.EmailField()
    ProfilePic=models.ImageField(upload_to='profile_pics',default='default.jpg')
    Mobile=models.IntegerField()
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.UserName
