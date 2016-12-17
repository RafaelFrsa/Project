# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('pressure', models.FloatField(verbose_name='Pressao')),
                ('density', models.FloatField(verbose_name='Densidade')),
                ('cp', models.FloatField(blank=True, verbose_name='CP')),
                ('viscosity', models.FloatField(verbose_name='Viscosidade')),
                ('k', models.FloatField(blank=True, verbose_name='k')),
                ('kt', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Agua',
                'verbose_name_plural': 'Aguas',
            },
        ),
        migrations.CreateModel(
            name='Butano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('pressure', models.FloatField(verbose_name='Pressao')),
                ('density', models.FloatField(verbose_name='Densidade')),
                ('cp', models.FloatField(verbose_name='CP')),
                ('viscosity', models.FloatField(verbose_name='Viscosidade')),
                ('k', models.FloatField(blank=True, verbose_name='k')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agua', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duplotubo.Agua')),
                ('Butano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duplotubo.Butano')),
            ],
        ),
        migrations.CreateModel(
            name='CO2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('pressure', models.FloatField(verbose_name='Pressao')),
                ('density', models.FloatField(verbose_name='Densidade')),
                ('cp', models.FloatField(verbose_name='CP')),
                ('viscosity', models.FloatField(verbose_name='Viscosidade')),
                ('k', models.FloatField(verbose_name='k')),
            ],
        ),
        migrations.CreateModel(
            name='Metano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('pressure', models.FloatField(verbose_name='Pressao')),
                ('density', models.FloatField(verbose_name='Densidade')),
                ('cp', models.FloatField(verbose_name='CP')),
                ('viscosity', models.FloatField(verbose_name='Viscosidade')),
                ('k', models.FloatField(verbose_name='k')),
            ],
        ),
        migrations.CreateModel(
            name='Pentano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('pressure', models.FloatField(verbose_name='Pressao')),
                ('density', models.FloatField(verbose_name='Densidade')),
                ('cp', models.FloatField(verbose_name='CP')),
                ('viscosity', models.FloatField(verbose_name='Viscosidade')),
                ('k', models.FloatField(verbose_name='k')),
            ],
        ),
        migrations.CreateModel(
            name='RC318',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='Temperatura')),
                ('pressure', models.FloatField(verbose_name='Pressao')),
                ('density', models.FloatField(verbose_name='Densidade')),
                ('cp', models.FloatField(verbose_name='CP')),
                ('viscosity', models.FloatField(verbose_name='Viscosidade')),
                ('k', models.FloatField(verbose_name='k')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.CharField(max_length=7000)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='CO2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duplotubo.CO2'),
        ),
        migrations.AddField(
            model_name='choice',
            name='Metano',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duplotubo.Metano'),
        ),
        migrations.AddField(
            model_name='choice',
            name='Pentano',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duplotubo.Pentano'),
        ),
        migrations.AddField(
            model_name='choice',
            name='RC318',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duplotubo.RC318'),
        ),
    ]
