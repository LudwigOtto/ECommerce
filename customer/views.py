from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Customer
from .forms import LoginForm, RegisterForm

# Create your views here.
def customer_list(request):
    #customers = Customer.objects.all()
    form = LoginForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cd = form.cleaned_data
        c_id = cd['c_id']
        #customer = get_object_or_404(Customer, customer_id = cd['c_id'])
    else:
        c_id = 0
        #customer = get_object_or_404(Customer, customer_id = 1)
    customer = get_object_or_404(Customer, customer_id = c_id)
    return render(request,
                  'customer/list.html',
                  {'customer': customer})

def customer_new(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        c_id = cd['c_id']
        c_first = cd['firstN']
        c_last = cd['lastN']
        c_email = cd['email']
        c_phone = cd['phone']
        c_addr = cd['address']
        customer = Customer.objects.create(customer_id=c_id,
                email=c_email,
                first_name=c_first,
                last_name=c_last,
                phone_number=c_phone,
                address=c_addr)
    return render(request,
                  'customer/list.html',
                  {'customer': customer})

def customer_signIn(request):
    loginForm = LoginForm()
    return render(request, 'customer/login.html', {'loginForm': LoginForm})

def customer_signUp(request):
    registerForm = RegisterForm()
    return render(request, 'customer/register.html', {'registerForm': RegisterForm})
