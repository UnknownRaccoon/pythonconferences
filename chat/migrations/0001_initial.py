# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0006_auto_20160609_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('recipient', models.ForeignKey(related_name='recipient', to='custom_auth.Profile')),
                ('sender', models.ForeignKey(related_name='sender', to='custom_auth.Profile')),
            ],
        ),
    ]
