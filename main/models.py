from django.db import models

class Client(models.Model):
    
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    order = models.CharField(max_length=300)
    
    def as_dict(self):
        
        return {
            
            'pk': self.pk,
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'order': self.order
            
        }
    
    
class MenuItem(models.Model):
    
    TYPES = (
        ('PZ', 'بيتزا'),
        ('MC', 'مكرونات'),
        ('SW', 'حلو'),
        ('SO', 'حادق')
    )
    
    name = models.CharField(max_length=300)
    item_type = models.CharField(max_length=2, choices=TYPES)
    medium_price = models.FloatField()
    large_price = models.FloatField()
    components = models.TextField()
    
    
class Order(models.Model):
    
    TYPES = (
        ('IN', 'صالة'),
        ('DL', 'ديليفرى'),
        ('TA', 'تيك أواى')
    )
    
    client = models.ForeignKey(Client, related_name='orders')
    order_type = models.CharField(max_length=2, choices=TYPES)
    total_cost = models.FloatField(default=0)
    notes = models.CharField(max_length=300)
    
    def as_dict(self):
        
        return {
            
            'id': self.id,
            'type': self.order_type,
            'total_cost': self.total_cost,
            'notes': self.notes,
            'items': [item.as_dict() for item in self.items.all()]
            
        }
    

class OrderItem(models.Model):
    
    item = models.ForeignKey(MenuItem, related_name='order_items')
    order = models.ForeignKey(Order, related_name='items')
    
    count = models.IntegerField()
    
    def as_dict(self):
                
        return {
            
            'id': self.id,
            'name': self.item.name,
            'count': self.count
            
        }