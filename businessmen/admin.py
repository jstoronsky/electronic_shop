from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext

from businessmen.models import Businessman, Product


# Register your models here.


@admin.register(Businessman)
class BusinessmanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'supplier_link', 'debt', 'created')
    list_filter = ('city', )
    actions = ['clear_debt']

    @admin.action(description="Clear debts")
    def clear_debt(self, request, queryset):
        updated = queryset.update(debt=0.0)
        self.message_user(
            request,
            ngettext(
                "%d debt was successfully cleared.",
                "%d debts were successfully cleared.",
                updated
            )
            % updated,
            messages.SUCCESS,
        )

    def supplier_link(self, obj):
        if obj.supplier.factory is not None:
            url = reverse("admin:chain_factory_change", args=[obj.supplier.factory.id])
            link = '<a href="%s">%s</a>' % (url, obj.supplier.factory.name)
            return mark_safe(link)
        else:
            url = reverse("admin:retailers_retailer_change", args=[obj.supplier.retailer.id])
            link = '<a href="%s">%s</a>' % (url, obj.supplier.retailer.name)
            return mark_safe(link)

    supplier_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'seller', 'release_date')
    list_filter = ('seller', )
