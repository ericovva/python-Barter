# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20161211_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorysubcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='service.Category'),
        ),
        migrations.AlterField(
            model_name='categorysubcategory',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='service.Category'),
        ),
    ]