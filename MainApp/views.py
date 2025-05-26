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
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Товар {item['id']}</title>
            <style>
                body {{ font-family: Arial; margin: 20px; }}
                a {{ color: #0066cc; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
            </style>
        </head>
        <body>
            <h1>Информация о товаре</h1>
            <p><strong>ID:</strong> {item['id']}</p>
            <p><strong>Название:</strong> {item['name']}</p>
            <p><strong>Количество:</strong> {item['quantity']}</p>
            <p><a href="/items/">← Назад к списку товаров</a></p>
        </body>
        </html>
        """
        return HttpResponse(html)
    except IndexError:
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ошибка</title>
            <style>
                body {{ font-family: Arial; margin: 20px; color: red; }}
            </style>
        </head>
        <body>
            <h1>Товар не найден</h1>
            <p>Товар с id={item_id} не существует</p>
            <p><a href="/items/">← Назад к списку товаров</a></p>
        </body>
        </html>
        """
        return HttpResponse(html, status=404)

def items_list(request):
    items_html = ""
    for item in items_df.to_dict('records'):
        items_html += f"""
        <li>
            <a href="/item/{item['id']}/">{item['name']}</a>
        </li>
        """
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Список товаров</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            ol {{ line-height: 1.6; }}
            a {{ color: #0066cc; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h1>Список товаров</h1>
        <ol>
            {items_html}
        </ol>
    </body>
    </html>
    """
    return HttpResponse(html)
