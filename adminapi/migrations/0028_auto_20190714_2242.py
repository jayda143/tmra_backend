# Generated by Django 2.2.1 on 2019-07-14 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0027_auto_20190714_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individualpoints',
            old_name='non_billiable',
            new_name='non_billable',
        ),
        migrations.RenameField(
            model_name='individualpoints',
            old_name='notpaid_billiable',
            new_name='notpaid_billable',
        ),
    ]
