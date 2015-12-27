# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_auto_20151226_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=100)),
                ('profesor', models.ForeignKey(to='perfiles.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grado', models.CharField(max_length=1, choices=[(b'1', b'Primero'), (b'2', b'Segundo'), (b'3', b'Tercero'), (b'4', b'Cuarto'), (b'5', b'Quinto'), (b'6', b'Sexto')])),
                ('seccion', models.CharField(max_length=1)),
                ('fec_reserva', models.DateTimeField(auto_now_add=True)),
                ('pago', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('fec_confirma', models.DateTimeField()),
                ('alumno', models.ForeignKey(to='perfiles.Alumno')),
                ('curso', models.ForeignKey(to='matricula.Curso')),
            ],
        ),
    ]
