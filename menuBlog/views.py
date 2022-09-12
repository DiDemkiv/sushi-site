import json

from django.shortcuts import render, get_object_or_404
from .models import Section, Dish, Currency
from google_currency import convert


def menu_page(request):
    currency = request.GET.get("currency", "UAH")
    sections = Section.objects.all().order_by('numbering')
    dishes = Dish.objects.all()
    currencies = Currency.objects.all()
    currency_symbol = currencies.get(name=currency).symbol
    if currency != "UAH":
        rate = float(json.loads(convert("UAH", currency, 1)).get("amount"))
        for dish in dishes:
            dish.price = round(dish.price * rate, 2)
    return render(request, 'menuBlog/menu_page.html',
                  {'sections': sections, 'currencies': currencies, 'dishes': dishes, "currentCurrency": currency_symbol})


def dish_detail(request, name):
    dish = get_object_or_404(Dish, name=name)
    return render(request, 'menuBlog/dish_detail.html', {'dish': dish})
