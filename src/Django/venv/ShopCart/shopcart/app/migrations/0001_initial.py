# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Price', models.IntegerField()),
                ('Title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ProductTypes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ProdTypeId',
            field=models.ForeignKey(db_column='ProdTypeId', related_name='Products_ProductTypes', to='app.ProductType'),
        ),
    ]
