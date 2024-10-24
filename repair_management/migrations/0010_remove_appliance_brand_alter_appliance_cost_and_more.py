# Generated by Django 5.1.1 on 2024-10-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_management', '0009_rename_name_appliance_appliance_type_appliance_model_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliance',
            name='brand',
        ),
        migrations.AlterField(
            model_name='appliance',
            name='cost',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='exp_end_of_life',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='make',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='model',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
