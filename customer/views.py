from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Customer
from .forms import LoginForm, RegisterForm

# Create your views here.
def customer_list(request, c_id = 1):
    #customers = Customer.objects.all()
    customer = get_object_or_404(Customer, customer_id = c_id)
    return render(request,
                  'customer/list.html',
                  {'customer': customer})

def customer_signIn(request):
    loginForm = LoginForm()
    return render(request, 'customer/login.html', {'loginForm': LoginForm})

def customer_signUp(request):
    registerForm = RegisterForm()
    return render(request, 'customer/register.html', {'registerForm': RegisterForm})
