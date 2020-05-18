# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('amount_off', models.FloatField(help_text='Enter the amount of money or percentage to be deducted')),
                ('type', models.CharField(choices=[('MON', 'Money to be removed'), ('DIS', 'Discount to apply')], max_length=20)),
                ('valid', models.BooleanField(default=True)),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]