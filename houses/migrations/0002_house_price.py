# Generated by Django 3.2.7 on 2021-10-04 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
            preserve_default=False,
        ),
    ]
