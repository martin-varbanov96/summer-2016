# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('page_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Thread'),
        ),
    ]
