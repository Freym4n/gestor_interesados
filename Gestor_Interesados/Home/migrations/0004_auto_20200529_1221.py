# Generated by Django 3.0.3 on 2020-05-29 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20200529_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='id_servicio',
            new_name='servicio',
        ),
    ]
