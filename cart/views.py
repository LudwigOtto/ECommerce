from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Inventory
#from .cart import Cart
from .forms import CartAddProductForm
from customer.models import Customer
from .models import Item

@require_POST
def cart_add(request, item_id):
    product = get_object_or_404(Inventory, item_id=item_id)
    customer = get_object_or_404(Customer, customer_id=1)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        """
        cart.add(item=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        """
        Item.objects.create(item_id=product,
                                price=product.price,
                                type=product.type,
                                seller=product.seller,
                                customer_id=customer,
                                quantity_per_item=cd['quantity'])

    return redirect('cart:cart_detail')

def cart_detail(request):
    items = Item.objects.all()
    """
    for item in items:
        inventory = item.item_id
    """
    """
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })
    """
    return render(request, 'cart/detail.html', {'items': items}
                )
