from django.db import models

# Create your models here.
class Tasks(models.Model):
    moduleName = models.CharField(max_length=100, blank=False, null=False)
    taskName = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=20)
    order=models.IntegerField()
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
        return self.taskName+self.code
