from django.utils import timezone

from expenses.models import *
from expenses import utils as expenses_utils
from main.models import *

import json

def update_cell_content(pk, item_type, field_name, content):
    
    changes = {}
    
    if item_type == 'expense':
        
        expense = Expense.objects.get(pk=pk)
        
        if field_name == 'formatted_balance_change':
            
            new_balance_change = float(content)
            
            old_balance_change = expense.balance_change
            
            if new_balance_change == old_balance_change:
                return True, changes
            
            expense.update_total_after_change(new_balance_change)
            
            changes['new_totals'] = expense.get_new_totals(old_balance_change)
            
            changes['current_balance'], daily_expense = expenses_utils.update_daily_expense()
            changes['daily_expense'] = daily_expense.as_dict(include_closing_data=True)
            
        elif field_name == 'description':
            
            expense.description = content
            expense.save()
        
    return True, changes

def prepare_post_data():
    
    daily_expense = DailyExpense.objects.get(date=timezone.now().date())
    
    revenue_items = [expense.as_post_data_dict() for expense in Expense.objects.filter(date=daily_expense.date, balance_change__gt=0)]
    expense_items = [expense.as_post_data_dict() for expense in Expense.objects.filter(date=daily_expense.date, balance_change__lt=0)]
    
    indoor_orders_count = Order.objects.filter(order_type='IN').count()
    delivery_orders_count = Order.objects.filter(order_type='DL').count()
    takeaway_orders_count = Order.objects.filter(order_type='TA').count()
    all_orders_count = Order.objects.count()
    
    indoor_perc  = (indoor_orders_count / all_orders_count) * 100
    delivery_perc  = (indoor_orders_count / all_orders_count) * 100
    takeaway_perc  = (indoor_orders_count / all_orders_count) * 100
    
    data = {
        'revenue_items': revenue_items,
        'expense_items': expense_items,
        
        'order_percentages': {
            'indoor_percentage': indoor_perc,
            'delivery_percentage': delivery_perc,
            'takeaway_percentage': takeaway_perc
        }
    }
    
    data = {'data': json.dumps(data)}
    
    return data