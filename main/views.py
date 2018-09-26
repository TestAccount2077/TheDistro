from django.shortcuts import render
from django.http import JsonResponse

from .models import *

import json

def todays_orders(request):
    
    context = {
        'Order': Order.objects,
        'clients': Client.objects.all(),
        'orders': {order.id: order.as_dict() for order in Order.objects.all()}
    }
    
    return render(request, 'main/todays_orders.html', context=context)


def add_client(request):
    
    data = request.GET
    
    client = Client.objects.create(
        name=data['name'],
        phone=data['phone'],
        address=data['address'],
        order=data['order']
    )
    
    return JsonResponse({'client': client.as_dict()})

def remove_order(request):
    
    Order.objects.get(pk=request.GET['pk']).delete()
    
    return JsonResponse({})

def new_order(request):
    
    data = request.GET
    context = {}
    
    if data.get('items'):
        context['items'] = json.loads(data['items'])
        context['data'] = json.loads(data['data'])
    
    return render(request, 'main/new-order.html', context=context)

def menu_view(request):
    
    context = {
        'items': MenuItem.objects.all()
    }
    
    return render(request, 'main/menu.html', context=context)

def inquire_client(request):
    
    if request.is_ajax():
        
        context = {}
        phone = request.GET['phone']
        
        client = Client.objects.filter(phone=phone)
        
        if client.exists():
            client = client.first()
            context['client'] = client.as_dict()
            
        else:
            context['not_found'] = True
        
        return JsonResponse(context)

def order_menu(request):
    
    data = request.GET
    
    context = {
        
        'data': json.dumps({
            'name': data['name'],
            'address': data['address'],
            'phone': data['phone']
        }),
        
        'items': MenuItem.objects.all()
    }
    
    return render(request, 'main/order-menu.html', context=context)

def create_order(request):
    
    if request.is_ajax():
        
        data = request.GET
        items = json.loads(data['items'])
        client_data = json.loads(data['data'])
        
        client, created = Client.objects.get_or_create(phone=client_data['phone'])
        
        if created:
            
            client.name = client_data['name']
            client.address = client_data['address']
            
            client.save()
        
        order = Order.objects.create(client=client)
        
        for item in items:
            
            menu_item = MenuItem.objects.get(name=item['name'])
            count = int(item['count'])
            
            order.total_cost += menu_item.medium_price * count
            
            order.items.create(
                item=menu_item,
                count=count
            )
        
        order.save()
        
        return JsonResponse({})
