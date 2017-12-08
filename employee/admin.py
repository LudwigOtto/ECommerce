from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['employee_id', 'role', 'data_joined', 'supervisor_id']
	list_editable = ['role', 'supervisor_id']


admin.site.register(Employee, EmployeeAdmin)