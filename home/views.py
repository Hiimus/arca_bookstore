from django.shortcuts import render
from products.models import Product

import random

# Create your views here.


def index(request):
    """ Home page with a randomized sample of products """
    # Code inspired by:
    # https://stackoverflow.com/questions/22816704/django-get-a-random-object/23755881#23755881
    # Get objects by categories
    book_1 = list(Product.objects.filter(category=1))
    book_2 = list(Product.objects.filter(category=2))
    book_3 = list(Product.objects.filter(category=3))
    book_4 = list(Product.objects.filter(category=4))

    arts_and_craft_1 = list(Product.objects.filter(category=11))
    arts_and_craft_2 = list(Product.objects.filter(category=12))
    arts_and_craft_3 = list(Product.objects.filter(category=13))
    arts_and_craft_4 = list(Product.objects.filter(category=12))

    game_1 = list(Product.objects.filter(category=14))
    game_2 = list(Product.objects.filter(category=15))
    game_3 = list(Product.objects.filter(category=14))
    game_4 = list(Product.objects.filter(category=15))

    # Get a random sample
    # change 1 to how many random items you want
    books_1 = random.sample(book_1, 1)
    books_2 = random.sample(book_2, 1)
    books_3 = random.sample(book_3, 1)
    books_4 = random.sample(book_4, 1)

    arts_and_crafts_1 = random.sample(arts_and_craft_1, 1)
    arts_and_crafts_2 = random.sample(arts_and_craft_2, 1)
    arts_and_crafts_3 = random.sample(arts_and_craft_3, 1)
    arts_and_crafts_4 = random.sample(arts_and_craft_4, 1)

    games_1 = random.sample(game_1, 1)
    games_2 = random.sample(game_2, 1)
    games_3 = random.sample(game_3, 1)
    games_4 = random.sample(game_4, 1)

    context = {
        'books_1': books_1,
        'books_2': books_2,
        'books_3': books_3,
        'books_4': books_4,
        'arts_and_crafts_1': arts_and_crafts_1,
        'arts_and_crafts_2': arts_and_crafts_2,
        'arts_and_crafts_3': arts_and_crafts_3,
        'arts_and_crafts_4': arts_and_crafts_4,
        'games_1': games_1,
        'games_2': games_2,
        'games_3': games_3,
        'games_4': games_4,
    }

    return render(request, 'home/index.html', context)
