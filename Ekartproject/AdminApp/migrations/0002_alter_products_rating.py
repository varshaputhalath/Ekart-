# Generated by Django 5.1.4 on 2024-12-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
