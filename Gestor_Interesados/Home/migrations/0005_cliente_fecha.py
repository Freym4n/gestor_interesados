# Generated by Django 3.0.3 on 2020-05-29 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20200529_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
