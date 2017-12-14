from django.contrib import admin

# Register your models here.
from .models import Item


class ItemAdmin(admin.ModelAdmin):
	list_display = ['item_id', 'price', 'type', 'seller',
					'customer_id', 'quantity_per_item', 'total_price' ]


admin.site.register(Item, ItemAdmin)