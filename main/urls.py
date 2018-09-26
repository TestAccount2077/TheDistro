from django.conf.urls import url
from .views import *

app_name = 'main'

urlpatterns = [

    # HTTP URLs
    url(r'^$', todays_orders),
    url(r'^new-order/$', new_order),
    url(r'^menu/', menu_view),
    url(r'order-menu/$', order_menu),

    # AJAX URLs
    url(r'^ajax/add-client/$', add_client),
    url(r'^ajax/remove-order/$', remove_order),
    url(r'^ajax/inquire-client/$', inquire_client),
    url(r'^ajax/create-order/$', create_order),

]
