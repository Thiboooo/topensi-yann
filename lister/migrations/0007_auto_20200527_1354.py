# Generated by Django 3.0.6 on 2020-05-27 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lister', '0006_auto_20200527_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='client',
            new_name='cli',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='type',
            new_name='typ',
        ),
    ]
