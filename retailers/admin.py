from django.contrib import admin, messages
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext

from retailers.models import Retailer, Product


# Register your models here.
@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
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
            url = reverse("admin:businessmen_businessman_change", args=[obj.supplier.businessman.id])
            link = '<a href="%s">%s</a>' % (url, obj.supplier.businessman.name)
            return mark_safe(link)

    supplier_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'retailer', 'release_date')
    list_filter = ('retailer', )
