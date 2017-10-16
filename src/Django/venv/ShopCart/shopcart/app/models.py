from django.db import models

# Create your models here.


class Product(models.Model):

    Id = models.AutoField(primary_key=True)
    Price = models.IntegerField(null=False)
    Title = models.CharField(max_length=100, null=False)
    ProdType = models.ForeignKey('ProductType', db_column='ProdType', related_name='Products_ProductTypes')

    def __str__(self):
        return self.Title

    class Meta(object):
        db_table = "Products"


class ProductType(models.Model):

    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.Name

    class Meta(object):
        db_table = "ProductTypes"
