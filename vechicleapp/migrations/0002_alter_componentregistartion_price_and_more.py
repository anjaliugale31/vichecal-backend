# Generated by Django 5.1.4 on 2024-12-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechicleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentregistartion',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='componentregistartion',
            name='repair_cost',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
