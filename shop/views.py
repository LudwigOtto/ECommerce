from django.shortcuts import render, get_object_or_404
from .models import Inventory

def inventory_list(request):
    #inventories = Inventory.objects.filter(lambda x: x > 0, quantity)
    inventories = Inventory.objects.all()
    return render(request,
                  'shop/list.html',
                  {'inventories': inventories})
# Create your views here.

def inventory_detail(request, item_id):
    inventory = get_object_or_404(Inventory,
                                item_id=item_id)
    #inventories = Inventory.objects.filter(item_id=pid)
    # cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/detail.html',
                  {'inventory': inventory})
                  #{'inventory': inventories,
                  # 'cart_product_form': cart_product_form})