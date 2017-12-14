from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer_list(request, c_id = 1):
    #customers = Customer.objects.all()
    customer = get_object_or_404(Customer, customer_id = c_id)
    return render(request,
                  'customer/list.html',
                  {'customer': customer})
