# Generated by Django 2.2.1 on 2019-05-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopbranchoutlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbo',
            name='area_square_ft',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sbo',
            name='is_branch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sbo',
            name='is_outlet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sbo',
            name='is_shop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sbo',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sbo',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sbo',
            name='no_of_employees',
            field=models.IntegerField(null=True),
        ),
    ]
