from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist

from .forms import ShipForm, PayForm
from .models import Payment, Shipment
from customer.models import Customer
from shop.models import Inventory

# Create your views here.
# @require_POST

def shipment_view(request):
    shipForm = ShipForm()
    return render(request, 'orders/ship.html', {'ShipForm': ShipForm})

def payment_view(request):
    payForm = PayForm()
    return render(request, 'orders/pay.html', {'PayForm': PayForm})

def shipment_add(request):
    customer = get_object_or_404(Customer, customer_id=Customer.CUR_ID)
    try:
        Shipment.objects.get(customer_id=customer)
        return redirect('orders:payment')
    except ObjectDoesNotExist:
        form = ShipForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            c_type = cd['ship_type']
            c_detail = cd['ship_detail']
            c_address = cd['address']
            Shipment.objects.create(customer_id=customer,
                    physical_address=c_address,
                    shipment_type=c_type,
                    shipment_detail=c_detail)
            return redirect('orders:payment')


def payment_add(request):
    customer = get_object_or_404(Customer, customer_id=Customer.CUR_ID)
    try:
        Payment.objects.get(customer_id=customer)
        return render(request, 'orders/Thanks.html')
    except ObjectDoesNotExist:
        form = PayForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            c_id = customer
            c_type = cd['pay_Type']
            c_cardnum = cd['card_num']
            c_carddate = cd['card_date']
            Payment.objects.create(customer_id=c_id,
                    payment_type=c_type,
                    card_expire_date=c_carddate,
                    card_number=c_cardnum)
            return render(request, 'orders/Thanks.html')
            #inventories = Inventory.objects.all()
            #return render(request,'shop/list.html', {'inventories': inventories})

"""
def order_detail(request, customer_id):
    orders = ShoppingCart.objects.filter(customer_id=customer_id)
    return render(request, 'orders/detail.html', {'orders': orders})
"""
