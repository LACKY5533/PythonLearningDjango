import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

items_df = pd.DataFrame([
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124}
])

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def item_detail(request, item_id):
    items = items_df.to_dict('records')
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return render(request, 'item_detail.html', status=404)
    return render(request, 'item_detail.html', {'item': item})

def items_list(request):
    # Конвертируем DataFrame в список словарей
    items = items_df.to_dict('records')
    
    return render(request, 'items_list.html', {
        'items': items
    })
