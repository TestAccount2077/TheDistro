from django.db import models

class TimeStampedModel(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    deleted = models.BooleanField(default=False)
    
    class Meta:
        
        abstract = True
        ordering = ('created',)


class App(models.Model):
    
    password = models.CharField(max_length=255, null=True, blank=True)
    
    current_balance = models.FloatField(default=0.0)
    

