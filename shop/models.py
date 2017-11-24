from __future__ import unicode_literals
from django.db import models


class Inventory(models.Model):
    item_id = models.IntegerField(db_column='Item Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_name = models.CharField(db_column='Item Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    seller = models.CharField(db_column='Seller', max_length=45)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventory'
