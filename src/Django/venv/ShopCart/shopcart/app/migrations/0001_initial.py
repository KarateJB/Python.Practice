# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

# Initialize ProductTypes
def initProdustTypes(apps, schema_editor):
    ptModel = apps.get_model("app", "ProductType") #apps.get_model(app_label, model_name, require_ready=True)
    ptDataBook = ptModel(Name='Book')
    ptDataBook.save()
    ptDataClothes = ptModel(Name='Clothes')
    ptDataClothes.save()
    ptDataToy = ptModel(Name='Toy')
    ptDataToy.save()
    

# Remove all records in ProductTypes
def removeProductTypes(apps, schema_editor):
    ptModel = apps.get_model("app", "ProductType") #apps.get_model(app_label, model_name, require_ready=True)
    ptModel.objects.all().delete()


def initProdustTypesSql():
    
    sql = """
      INSERT INTO ProductTypes(Name) VALUES('Book');
      INSERT INTO ProductTypes(Name) VALUES('Clothes');
      INSERT INTO ProductTypes(Name) VALUES('Toy');
    """
    return sql

def removeProductTypesSql():
    return 'DELETE from ProductTypes'    


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
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
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ProductTypes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ProdType',
            field=models.ForeignKey(db_column='ProdType', related_name='Products_ProductTypes', to='app.ProductType'),
        ),
        migrations.RunPython(initProdustTypes,removeProductTypes)
        # migrations.RunSQL(initProdustTypesSql(), removeProductTypesSql())
    ]
