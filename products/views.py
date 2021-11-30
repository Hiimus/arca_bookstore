from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from itertools import chain


# Create your views here.

# Search bar
def search(request):
    q = request.GET['search']

    products = Book.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    artsandcrafts = ArtsAndCraft.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    games = Game.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))

    
    
    context = {
        'products': products,
        'artsandcrafts': artsandcrafts,
        'games': games,
        'q': q,
        'result_count': products.count() + artsandcrafts.count() + games.count()
    }

    return render(request, "products/search_products.html", context)



def all_books(request):
    """ A view to show all Books """

    products = Product.objects.all()

    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products_books.html', context)


def all_arts_and_crafts(request):
    """ A view to show all Arts & Crafts """

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products_artsandcraft.html', context)


def all_games(request):
    """ A view to show all games """

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products_games.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail/product_detail.html', context)


# def product_detail_arts(request, product_id):
#     """ A view to show individual product details """

#     artsandcraft = get_object_or_404(Product, pk=product_id)

#     context = {
#         'artsandcraft': artsandcraft,
#     }

#     return render(request, 'products/product_detail/product_detail.html', context)


# def product_detail_games(request, product_id):
#     """ A view to show individual product details """

#     game = get_object_or_404(Product, pk=product_id)

#     context = {
#         'game': game,
#     }

#     return render(request, 'products/product_detail/product_detail.html', context)

