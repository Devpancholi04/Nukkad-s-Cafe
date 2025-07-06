from django.shortcuts import render
from .models import MenuItem, Testimonials, Category
from .serializers import MenuItemSerializer, TestimonialsSerializer, CategorySerializer

from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


# Create your views here.
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def index(request):

    menu_cache_key = "MENU-ITEM-CACHE"
    menu_items = cache.get(menu_cache_key)

    if not menu_items:
        queryset = MenuItem.objects.filter(is_available = True)
        serializers = MenuItemSerializer(queryset, many=True)
        menu_items = serializers.data
        cache.set(menu_cache_key, menu_items, timeout=CACHE_TTL) 

    testimonials_cache_key = "TESTIMONIALS-CACHE-KEY"
    testimonials = cache.get(testimonials_cache_key)

    if not testimonials:
        test_queryset = Testimonials.objects.filter(is_active = True)
        test_serializers = TestimonialsSerializer(test_queryset, many = True)
        testimonials = test_serializers.data
        cache.set(testimonials_cache_key, testimonials, timeout=CACHE_TTL)


    context = {
        "menu_items" : menu_items[:8],
        "testimonials" : testimonials,
    }

    return render(request, 'home/home.html', context)

def menu(request):

    category_cache_key = "CATEGORY-CACHE-KEY"
    category = cache.get(category_cache_key)

    if not category:
        category_queryset = Category.objects.all()
        category_serializers = CategorySerializer(category_queryset, many = True)
        category = category_serializers.data
        cache.set(category_cache_key, category, timeout=CACHE_TTL)


    menu_cache_key = "MENU-ITEM-CACHE"
    menu_items = cache.get(menu_cache_key)

    if not menu_items:
        queryset = MenuItem.objects.filter(is_available = True)
        serializers = MenuItemSerializer(queryset, many=True)
        menu_items = serializers.data
        cache.set(menu_cache_key, menu_items, timeout=CACHE_TTL) 


    context = {
        "categories" : category,
        "menu_items" : menu_items,
    }

    return render(request, "home/menu.html", context)


def orders(request, tableid):

    category_cache_key = "CATEGORY-CACHE-KEY"
    category = cache.get(category_cache_key)

    if not category:
        category_queryset = Category.objects.all()
        category_serializers = CategorySerializer(category_queryset, many = True)
        category = category_serializers.data
        cache.set(category_cache_key, category, timeout=CACHE_TTL)


    menu_cache_key = "MENU-ITEM-CACHE"
    menu_items = cache.get(menu_cache_key)

    if not menu_items:
        queryset = MenuItem.objects.filter(is_available = True)
        serializers = MenuItemSerializer(queryset, many=True)
        menu_items = serializers.data
        cache.set(menu_cache_key, menu_items, timeout=CACHE_TTL) 


    context = {
        "tableid" : tableid,
        "categories" : category,
        "menu_items" : menu_items,
    }

    return render(request, "home/orders.html", context)