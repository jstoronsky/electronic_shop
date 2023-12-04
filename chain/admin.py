from django.contrib import admin
from chain.models import Factory, Product
# Register your models here.


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'country', 'created')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'manufacturer', 'release_date')
    list_filter = ('manufacturer', )
