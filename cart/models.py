from __future__ import unicode_literals
from django.db import models
from shop.models import Inventory
from customer.models import Customer

class Item(models.Model):
    item_id = models.ForeignKey(Inventory, models.DO_NOTHING, db_column='Item Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    seller = models.CharField(db_column='Seller', max_length=45)  # Field name made lowercase.
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer Id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity_per_item = models.IntegerField(db_column='Quantity per Item')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Item'
        unique_together = (('item_id', 'customer_id'),)

