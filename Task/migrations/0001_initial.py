# Generated by Django 2.2.1 on 2019-05-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('moduleName', models.CharField(max_length=100)),
                ('taskName', models.CharField(max_length=100)),
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('view_task', models.BooleanField(default=False)),
                ('add_task', models.BooleanField(default=False)),
                ('save_task', models.BooleanField(default=False)),
                ('edit_task', models.BooleanField(default=False)),
                ('delete_task', models.BooleanField(default=False)),
                ('print_task', models.BooleanField(default=False)),
                ('cancel_task', models.BooleanField(default=False)),
                ('reset_task', models.BooleanField(default=False)),
                ('find_task', models.BooleanField(default=False)),
            ],
        ),
    ]
