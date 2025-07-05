from django.shortcuts import render
from .models import MenuItem, Testimonials
from .serializers import MenuItemSerializer, TestimonialsSerializer

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