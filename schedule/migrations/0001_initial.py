# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.CharField(default=b'', max_length=30)),
                ('company', models.CharField(default=b'', max_length=30, blank=True)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(default=b'', max_length=100)),
                ('ended', models.BooleanField(default=True)),
                ('priority', models.CharField(default=(2, b'Standard'), max_length=1, choices=[(1, b'Important'), (2, b'Standard'), (3, b'Casual')])),
                ('user', models.ForeignKey(related_name='meetings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
