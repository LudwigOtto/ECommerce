# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

"""
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
"""
"""
class Employee(models.Model):
    employee_id = models.IntegerField(db_column='Employee Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    role = models.CharField(db_column='Role', max_length=45)  # Field name made lowercase.
    data_joined = models.DateTimeField(db_column='Data Joined')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supervisor_id = models.ForeignKey('self', models.DO_NOTHING, db_column='Supervisor Id', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Employee'
"""
"""
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
"""
"""
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
"""

class Payment(models.Model):
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    card_number = models.CharField(db_column='Card Number', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    card_expire_date = models.DateTimeField(db_column='Card Expire Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_type = models.CharField(db_column='Payment Type', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Payment'
        unique_together = (('customer_id', 'card_number'),)


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


class Shipment(models.Model):
    physical_address = models.TextField(db_column='Physical Address')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipment_type = models.CharField(db_column='Shipment Type', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shipment_detail = models.CharField(db_column='Shipment Detail', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Shipment'
        unique_together = (('customer_id', 'shipment_detail'),)

"""
class ShoppingCart(models.Model):
    customer_id = models.ForeignKey(Item, models.DO_NOTHING, db_column='Customer Id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_name = models.CharField(db_column='Item Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantity_per_item = models.IntegerField(db_column='Quantity per Item')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price_per_item = models.IntegerField(db_column='Price per Item')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_id = models.ForeignKey(Item, models.DO_NOTHING, db_column='Item Id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shopping_cart_id = models.IntegerField(db_column='Shopping Cart Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purchased_date = models.DateTimeField(db_column='Purchased Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Shopping Cart'
        unique_together = (('shopping_cart_id', 'item_id'),)
"""

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
