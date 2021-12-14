from django.shortcuts import render
from products.models import Product

import random

# Create your views here.

def index(request):
    """ A view to return the home page """

    items = list(Product.objects.filter(category=1))

    items2 = list(Product.objects.filter(category=14))

    items3 = list(Product.objects.filter(category=12))

    # change 3 to how many random items you want
    products = random.sample(items, 4)

    games = random.sample(items2, 4)

    arts_and_crafts = random.sample(items3, 4)

    context = {
        'products': products,
        'games': games,
        'arts_and_crafts': arts_and_crafts,
    }

    return render(request, 'home/index.html', context)



