from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inventory_list,
        name='inventory_list'),
    url(r'^(?P<item_id>\d+)/$',
        views.inventory_detail,
        name='inventory_detail')
    ]

