# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(unique=True, max_length=50)),
                ('apellidos', models.CharField(max_length=60)),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('sexo', models.CharField(blank=True, max_length=10, verbose_name=b'G\xc3\xa9nero', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('fecha_nac', models.DateTimeField(auto_now=True)),
                ('lugar_nac', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(unique=True, max_length=50)),
                ('apellidos', models.CharField(max_length=60)),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('sexo', models.CharField(blank=True, max_length=10, verbose_name=b'Encargado', choices=[(b'M', b'Padre'), (b'F', b'Madre')])),
                ('direccion', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(blank=True, max_length=10, verbose_name=b'Estado_civ\xc3\xadl', choices=[(b'M', b'Padre'), (b'F', b'Madre')])),
                ('telefono', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=50)),
                ('ocupacion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(unique=True, max_length=50)),
                ('apellidos', models.CharField(max_length=60)),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('direccion', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=13)),
                ('fecha_nac', models.DateTimeField(auto_now=True)),
                ('imagen', models.ImageField(upload_to=b'profesores')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='encargado',
            field=models.ForeignKey(to='perfiles.Encargado'),
        ),
    ]
