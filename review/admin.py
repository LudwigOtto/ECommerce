from django.contrib import admin

# Register your models here.
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
	list_display = ['item_id', 'customer_id', 'seller', 
					'ratings', 'detailed_review'  ]
	list_editable = ['ratings', 'detailed_review' ]


admin.site.register(Review, ReviewAdmin)