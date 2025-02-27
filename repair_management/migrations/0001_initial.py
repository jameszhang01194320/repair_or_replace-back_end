# Generated by Django 5.1.1 on 2024-10-16 23:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('exp_end_of_life', models.DateField()),
                ('purchase_date', models.DateField()),
                ('current_status', models.CharField(choices=[('working', 'Working'), ('needs repair', 'Needs Repair'), ('broken', 'Broken'), ('replaced', 'Replaced')], max_length=20)),
                ('cost', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliances', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_type', models.CharField(choices=[('replacement', 'Replacement'), ('maintenance', 'Maintenance'), ('repair', 'Repair'), ('upgrade', 'Upgrade')], max_length=25)),
                ('investment_date', models.DateField()),
                ('investment_description', models.CharField(max_length=250)),
                ('cost', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='repair_management.appliance')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=10)),
                ('home_type', models.CharField(choices=[('single', 'Single Family'), ('multi', 'Multi Family'), ('condo', 'Condo'), ('apartment', 'Apartment'), ('other', 'Other')], max_length=25)),
                ('year_built', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appliance',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliances', to='repair_management.property'),
        ),
        migrations.CreateModel(
            name='Repairs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_date', models.DateField()),
                ('repaired_by', models.CharField(max_length=250)),
                ('repaired_description', models.CharField(max_length=250)),
                ('cost', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repairs', to='repair_management.appliance')),
            ],
        ),
    ]
