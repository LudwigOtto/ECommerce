from django.conf.urls import url
from . import views

# Maybe no need to view customer
urlpatterns = [
    url(r'^$', views.customer_list),
]