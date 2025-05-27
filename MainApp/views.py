#import pandas as pd

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item
# Create your views here.

# items_df = pd.DataFrame([
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124}
# ])

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def items_list(request):
    items = Item.objects.all()  # Получаем все товары из БД
    return render(request, 'items_list.html', {'items': items})

def item_detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return render(request, 'item_detail.html', 
                    {'error': f'Товар с ID {item_id} не найден'},
                    status=404)
    
    return render(request, 'item_detail.html', {'item': item})
