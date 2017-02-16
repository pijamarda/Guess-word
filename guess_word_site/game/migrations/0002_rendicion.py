# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rendicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intentos', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(verbose_name='fecha')),
                ('palabra', models.ForeignKey(to='game.Palabra')),
            ],
        ),
    ]
