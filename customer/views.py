from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request,
                  'customer/list.html',
                  {'customers': customers})