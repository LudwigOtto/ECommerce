# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-14 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.ForeignKey(db_column='Item Id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='shop.Inventory')),
                ('price', models.IntegerField(db_column='Price')),
                ('type', models.CharField(blank=True, db_column='Type', max_length=45, null=True)),
                ('seller', models.CharField(db_column='Seller', max_length=45)),
                ('quantity_per_item', models.IntegerField(db_column='Quantity per Item')),
                ('total_price', models.IntegerField(db_column='Total_Price')),
            ],
            options={
                'db_table': 'Item',
                'managed': False,
            },
        ),
    ]