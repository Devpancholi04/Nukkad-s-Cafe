from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer

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

    context = {
        menu_items : menu_items[:8]
    }
    
    return render(request, 'home/home.html', context)