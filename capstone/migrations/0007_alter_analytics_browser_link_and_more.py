# Generated by Django 5.0.1 on 2024-02-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0006_analytics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='browser_link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='device_link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='os_link',
            field=models.CharField(max_length=100),
        ),
    ]
