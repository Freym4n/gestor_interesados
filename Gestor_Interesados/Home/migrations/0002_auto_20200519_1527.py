# Generated by Django 3.0.3 on 2020-05-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peticion',
            name='estado_revision',
            field=models.IntegerField(),
        ),
    ]
