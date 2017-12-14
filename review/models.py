from django.db import models

from shop.models import Inventory
from customer.models import Customer

# Create your models here.
class Review(models.Model):
    item_id = models.ForeignKey(Inventory, models.DO_NOTHING, db_column='Item Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer Id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seller = models.CharField(db_column='Seller', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ratings = models.IntegerField(db_column='Ratings')  # Field name made lowercase.
    detailed_review = models.TextField(db_column='Detailed Review', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Review'
        unique_together = (('item_id', 'customer_id'),)