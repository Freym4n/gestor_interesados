# Generated by Django 3.0.3 on 2020-05-19 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contenido_nosotros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_vision', models.CharField(max_length=4000)),
                ('desc_mision', models.CharField(max_length=4000)),
                ('desc_val_ser', models.CharField(max_length=4000)),
                ('desc_derechos', models.CharField(max_length=4000)),
                ('desc_escogenos', models.CharField(max_length=4000)),
                ('desc_te_ayudamos', models.CharField(max_length=4000)),
                ('desc_nuestros_clientes', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='contenido_servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ases_impuestos_tributaria', models.CharField(max_length=4000)),
                ('ases_administrativa_financiera', models.CharField(max_length=4000)),
                ('revisoria_fiscal', models.CharField(max_length=4000)),
                ('ases_contable', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=4000)),
                ('imagen', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=400)),
                ('fecha', models.DateField()),
                ('estado_revision', models.IntegerField(max_length=1)),
                ('id_Servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=15)),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Servicio')),
            ],
        ),
    ]