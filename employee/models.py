from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField(db_column='Employee Id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    role = models.CharField(db_column='Role', max_length=45)  # Field name made lowercase.
    data_joined = models.DateTimeField(db_column='Data Joined')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supervisor_id = models.ForeignKey('self', models.DO_NOTHING, db_column='Supervisor Id', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Employee'