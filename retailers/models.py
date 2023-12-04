from django.core.exceptions import ValidationError
from django.db import models

from chain.models import AbstractChain, Suppliers2, Suppliers1, AbstractProduct
from employers.models import NULLABLE


# Create your models here.

class Retailer(AbstractChain):
    supplier = models.ForeignKey('chain.Suppliers2', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='долг перед поставщиком')

    def __str__(self):
        return self.name

    def clean(self):
        for supplier in Suppliers2.objects.all():
            if self.supplier == supplier:
                if supplier.businessman is not None:
                    if supplier.businessman.supplier is not None and supplier.businessman.supplier.retailer is not None:
                        raise ValidationError('You can not choose this supplier because you serve as supplier to it.')

    def save(self, *args, **kwargs):
        super(Retailer, self).save(*args, **kwargs)
        if not Suppliers1.objects.filter(retailer=self).exists():
            sup = Suppliers1.objects.create(retailer=self)
            sup.save()

    class Meta:
        verbose_name = 'ритейлер'
        verbose_name_plural = 'ритейлеры'


class Product(AbstractProduct):
    retailer = models.ForeignKey('retailer', on_delete=models.CASCADE, verbose_name='ритейлер', **NULLABLE)
