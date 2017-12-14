from django.db import models
from cart.models import Item

# Create your models here.
#class ShoppingCart(models.Model):
#    customer_id = models.ForeignKey(Item, models.DO_NOTHING, db_column='Customer Id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#    item_name = models.CharField(db_column='Item Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#    quantity_per_item = models.IntegerField(db_column='Quantity per Item')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#    price_per_item = models.IntegerField(db_column='Price per Item')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#    item_id = models.ForeignKey(Item, models.DO_NOTHING, db_column='Item Id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#    shopping_cart_id = models.IntegerField(db_column='Shopping Cart Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#    purchased_date = models.DateTimeField(db_column='Purchased Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#    class Meta:
#        managed = False
#        db_table = 'Shopping Cart'
#        unique_together = (('shopping_cart_id', 'item_id'),)
