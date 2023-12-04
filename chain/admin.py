from django.contrib import admin
from chain.models import Factory, Retailer, Product, Businessman
# Register your models here.


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'country', 'created')


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'supplier', 'debt', 'created')
    list_filter = ('city', )


@admin.register(Businessman)
class BusinessmanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'supplier', 'debt', 'created')
    list_filter = ('city', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'manufacturer', 'release_date')
