# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=10, verbose_name=b'Estado_civ\xc3\xadl', choices=[(b'Soltero', b'Soltero(a)'), (b'Casado', b'Casado(a)'), (b'Viudo', b'Viudo(a)')]),
        ),
    ]
