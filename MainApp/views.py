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
    text = """
    <h1> "Изучаем django"</h1>
    <strong>Автор<strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text = """
    Имя: Иван
    Отчество: Петрович
    Фамилия: Иванов
    Телефон: 8-923-600-01-02
    Email: vasya@mail.ru
    """
    return HttpResponse(text, content_type="text/plain;charset=utf-8")


def item_detail(request, item_id):
    try:
        item = items_df[items_df['id'] == item_id].iloc[0]
        return render(request, 'item_detail.html', {
            'item': item
        })
    except IndexError:
        return render(request, 'error.html', {
            'item_id': item_id
        }, status=404)

def items_list(request):
    # Конвертируем DataFrame в список словарей
    items = items_df.to_dict('records')
    
    return render(request, 'items_list.html', {
        'items': items
    })
