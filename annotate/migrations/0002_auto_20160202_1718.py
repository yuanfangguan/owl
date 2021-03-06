# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.IntegerField(choices=[(1, 'CREATE'), (2, 'UPDATE'), (3, 'DELETE')])),
                ('anno', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.RenameField(
            model_name='annotation',
            old_name='text',
            new_name='anno',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='status',
        ),
        migrations.AddField(
            model_name='annotation',
            name='signature',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='meta',
            field=models.TextField(default='{}'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='log',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotate.Image'),
        ),
    ]
