from django.db import models
from Task.models import Tasks

# Create your models here.

class Roles(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name
class RoleDistribution(models.Model):
    Role=models.OneToOneField(Roles,on_delete=models.CASCADE)
    Task=models.OneToOneField(Tasks,on_delete=models.CASCADE)
    view_task = models.BooleanField(default=False)
    add_task = models.BooleanField(default=False)
    save_task = models.BooleanField(default=False)
    edit_task = models.BooleanField(default=False)
    delete_task = models.BooleanField(default=False)
    print_task = models.BooleanField(default=False)
    cancel_task = models.BooleanField(default=False)
    reset_task = models.BooleanField(default=False)
    find_task = models.BooleanField(default=False)

    def __str__(self):
        return self.Role.name
