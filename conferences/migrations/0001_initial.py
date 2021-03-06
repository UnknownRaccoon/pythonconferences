# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_auth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.BooleanField()),
                ('subject', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_auth.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='conference',
            name='participants',
            field=models.ManyToManyField(through='conferences.Participation', to='custom_auth.Profile'),
        ),
    ]
