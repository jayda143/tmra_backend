# Generated by Django 2.2.1 on 2019-07-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0009_auto_20190711_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='address',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
