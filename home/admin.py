from django.contrib import admin
from .models import *
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    search_fields = ['table_id','is_occupied']
    list_filter = ['is_occupied', 'created_at','updated_at']
    readonly_fields = ('table_id','created_at', 'updated_at')

    fieldsets = (
        ("TABLE DETAILS", {'fields' : ('table_id','is_occupied','qr_code')}),
        ("IMPORTANT DATES", {'fields' : ('created_at','updated_at')}),
    )

class TableSessionAdmin(admin.ModelAdmin):
    search_fields = ['session_id','table__table_id',]
    list_filter = ['table__table_id','created_at','active']
    readonly_fields = ('session_id','created_at')

    fieldsets = (
        ("TABLE SESSION DETAILS", {'fields' : ('session_id','table','active')}),
        ("IMPORTANT DATES", {'fields' : ('created_at',)})
    )

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_id','name']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ('category_id','created_at','updated_at')

    fieldsets = (
        ("CATEGORY DETAILS", {'fields' : ('category_id','name')}),
        ("IMPORTANT DATES", {'fields' : ('created_at', 'updated_at')})
    )

class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['menu_item_id','name','category__name','category_category_id',]
    list_filter = ['category__name','price','is_available','created_at','updated_at']
    readonly_fields = ('menu_item_id','created_at', 'updated_at')

    fieldsets = (
        ("MENU DETAILS", {'fields' : ('menu_item_id','name','category','description','images','price','is_available')}),
        ("IMPORTANT DATES", {'fields' : ('created_at','updated_at')})
    )

class TestimonailsAdmin(admin.ModelAdmin):
    search_fields = ['username', 'title',]
    list_filter = ['rating','is_active','created_at','updated_at']
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("TESTIMONAILS DETAILS", {'fields' : ('username','title','message','image','rating','is_active')}),
        ("IMPORTANT DATES", {'fields' : ('created_at','updated_at')})
    )

class CartItemAdmin(admin.StackedInline):
    model = CartItem
    search_fields = ['cart__cart_id','item__name','item__menu_item_id']
    list_filter = ['item__menu_item_id','quantity','added_at']
    readonly_fields = ('added_at',)

    fieldsets = (
        ('CART ITEMS DETAILS', {'fields' : ('cart','item','quantity')}),
        ('IMPORTANT_DATES', {'fields' : ('added_at',)})
    )

class CartAdmin(admin.ModelAdmin):
    search_fields = ['cart_id','session__session_id']
    readonly_fields = ('cart_id','created_at','updated_at')

    fieldsets = (
        ('CART DETAILS', {'fields' : ('cart_id','session')}),
        ('IMPORTANT DATES', {'fields' : ('created_at', 'updated_at')})
    )

    inlines = [CartItemAdmin]

class OrderItemAdmin(admin.StackedInline):
    model = OrderItem
    search_fields = ['order__order_id','item__name','item__menu_item_id']
    list_filter = ['item__menu_item_id','quantity', 'price','added_at']
    readonly_fields = ('added_at',)

    fieldsets = (
        ('ORDER ITEMS DETAILS', {'fields' : ('order','item','quantity','price')}),
        ('IMPORTANT DATES', {'fields' : ('added_at',)})
    )

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['order_id', 'session__session_id','cart__cart_id','payment_method','payment_status']
    list_filter = ['status','payment_method','payment_status','created_at','updated_at']
    readonly_fields = ('order_id','created_at','updated_at')

    fieldsets = (
        ('ORDER DETAILS', {'fields' : ('order_id', 'session','cart')}),
        ('ORDER STATUS', {'fields' : ('status', 'payment_method','payment_status', 'special_request')}),
        ('IMPORTANT DATES', {'fields' : ('created_at', 'updated_at')})
    )

    inlines = [OrderItemAdmin]


admin.site.register(Table, TableAdmin)
admin.site.register(TableSession, TableSessionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Testimonials, TestimonailsAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)