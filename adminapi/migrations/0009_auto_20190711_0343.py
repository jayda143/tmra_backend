# Generated by Django 2.2.1 on 2019-07-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0008_auto_20190711_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='address',
            field=models.CharField(default=True, max_length=500),
        ),
    ]