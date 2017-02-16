# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('intentos', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(verbose_name='fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reportada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=200)),
                ('veces', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='intento',
            name='palabra',
            field=models.ForeignKey(to='game.Palabra'),
        ),
    ]
