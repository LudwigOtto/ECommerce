from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist

from shop.models import Inventory
#from .cart import Cart
from .forms import CartAddProductForm
from customer.models import Customer
from .models import Item

@require_POST
def cart_add(request, item_id):
    product = get_object_or_404(Inventory, item_id=item_id)
    customer = get_object_or_404(Customer, customer_id=Customer.CUR_ID)
    form = CartAddProductForm(request.POST)#.__init__(target_id=product)
    form.match_quantity(item_id)            # for matching quantity
    if form.is_valid():
        cd = form.cleaned_data
        try:
            Item.objects.filter(item_id=item_id).update(quantity_per_item= cd['quantity'])
            per_price = Item.objects.get(item_id=item_id).price
            Item.objects.filter(item_id=item_id).update(total_price = per_price * cd['quantity'])
        except ObjectDoesNotExist:
            Item.objects.create(item_id=product,
                                price=product.price,
                                type=product.type,
                                seller=product.seller,
                                customer_id=customer,
                                quantity_per_item=cd['quantity'],
                                total_price = product.price * cd['quantity'])

    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    product = get_object_or_404(Inventory, item_id=item_id)
    try:
        Item.objects.filter(item_id=product).delete()
    except ObjectDoesNotExist:
        pass

    return redirect('cart:cart_detail')


def cart_detail(request):
    print(Customer.CUR_ID)
    items = Item.objects.filter(customer_id=Customer.CUR_ID)
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
    return render(request, 'cart/detail.html', {'items': items})
