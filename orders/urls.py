from django.conf.urls import url
from . import views

# Maybe no need to view customer
urlpatterns = [
    url(r'^ship$', views.shippment_add, name = 'shippment'),
    url(r'^payment$', views.payment_add, name = 'payment'),
]
