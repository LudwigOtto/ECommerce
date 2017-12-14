from django import forms
from .models import Item
from shop.models import Inventory

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
	# def __init__(self, target_id=20):
	# 	try:
	# 		quantity_per = Inventory.objects.get(item_id=target_id).quantity
	# 		print('################################')
	# 		print('Succeed Parse')
	# 		print(quantity_per)
	# 		QUANTITY_CHOICES = [(i, str(i)) for i in range(1, quantity_per+1)]
	# 		quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, 
	# 									  	  coerce=int)
	# 		update = forms.BooleanField(required=False,
	# 							initial=False,
	# 							widget=forms.HiddenInput)
	# 	except:
	# 		print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	# 		print('Fail parse')
	# 		pass
	#quantity_per = Item.objects.get(item_id=target_id).quantity_per_item
	#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, quantity_per+1)]
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, 
									  coerce=int)
	update = forms.BooleanField(required=False,
								initial=False,
								widget=forms.HiddenInput)

	def match_quantity(self, target_id=20):
		try:
			quantity_per = Inventory.objects.get(item_id=target_id).quantity
			print('################################')
			print('Succeed Parse')
			print(quantity_per)
			QUANTITY_CHOICES = [(i, str(i)) for i in range(1, quantity_per+1)]
			quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, 
										  	  coerce=int)
		except:
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			print('Fail parse')
			pass