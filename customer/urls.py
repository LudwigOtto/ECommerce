from django.conf.urls import url
from . import views

# Maybe no need to view customer
urlpatterns = [
    url(r'^(?P<c_id>\d+)/$', views.customer_list),
    url(r'^login$', views.customer_signIn, name='sign_in'),
    url(r'^register$', views.customer_signUp, name='sign_up'),
]
