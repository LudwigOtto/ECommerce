from django.conf.urls import url
from . import views

# Maybe no need to view customer
urlpatterns = [
    url(r'^ship$', views.shipment_view, name = 'shipment'),
    url(r'^shipAdd$', views.shipment_add, name = 'shipmentAdd'),
    url(r'^payment$', views.payment_view, name = 'payment'),
    url(r'^payAdd$', views.payment_add, name = 'paymentAdd'),
    #url(r'^detail$', views.order_view, name = 'order_detail'),
]
