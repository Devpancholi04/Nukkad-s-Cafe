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

admin.site.register(Table, TableAdmin)
admin.site.register(TableSession, TableSessionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Testimonials, TestimonailsAdmin)