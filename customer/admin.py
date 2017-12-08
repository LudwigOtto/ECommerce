from django.contrib import admin

# Register your models here.
from .models import Customer



class CustomerAdmin(admin.ModelAdmin):
	list_display = ['customer_id', 'email', 'first_name', 'last_name',
                    'phone_number', 'address']
	list_editable = ['email', 'phone_number',
					 'address']


admin.site.register(Customer, CustomerAdmin)