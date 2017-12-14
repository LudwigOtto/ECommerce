from django.contrib import admin

# Register your models here.
from .models import Inventory


class InventoryAdmin(admin.ModelAdmin):
	list_display = ['item_id', 'item_name', 'quantity',  'price', 
					'seller', 'type' ]
	list_editable = ['item_name', 'quantity',  'price', 
					'seller', 'type' ]


admin.site.register(Inventory, InventoryAdmin)