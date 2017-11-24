from django.shortcuts import render, get_object_or_404
from .models import Inventory

def inventory_list(request):
    #inventories = Inventory.objects.filter(Inventory.quantity > 0)
    inventories = Inventory.objects.all()
    return render(request,
                  'shop/list.html',
                  {'inventories': inventories})
# Create your views here.
