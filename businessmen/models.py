from django.core.exceptions import ValidationError
from django.db import models

from chain.models import AbstractChain, Suppliers1, Suppliers2
from employers.models import NULLABLE


# Create your models here.
class Businessman(AbstractChain):
    supplier = models.ForeignKey('chain.Suppliers1', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='долг перед поставщиком')
    objects = models.Manager()

    def __str__(self):
        return self.name

    def clean(self):
        for supplier in Suppliers1.objects.all():
            if self.supplier == supplier:
                if supplier.retailer is not None:
                    if supplier.retailer.supplier is not None and supplier.retailer.supplier.businessman is not None:
                        raise ValidationError('You can not choose this supplier because you serve as supplier to it.')

    def save(self, *args, **kwargs):
        super(Businessman, self).save(*args, **kwargs)
        if not Suppliers2.objects.filter(businessman=self).exists():
            sup = Suppliers2.objects.create(businessman=self)
            sup.save()

    class Meta:
        verbose_name = 'предприниматель'
        verbose_name_plural = 'предприниматели'


class Product(models.Model):
    name = models.CharField(max_length=35, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    seller = models.ForeignKey('businessman', on_delete=models.CASCADE, verbose_name='предприниматель', **NULLABLE)
    release_date = models.DateTimeField(verbose_name='дата выхода продукта')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

