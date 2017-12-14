from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.IntegerField(db_column='Customer Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', unique=True, max_length=45)  # Field name made lowercase.
    first_name = models.CharField(db_column='First Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='Phone Number', unique=True, max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'

    CUR_ID = 0
