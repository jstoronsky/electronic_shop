from django.core.exceptions import ValidationError
from django.db import models

from chain.models import AbstractChain, Suppliers1, Suppliers2, AbstractProduct
from employers.models import NULLABLE


# Create your models here.
class Businessman(AbstractChain):
    """
    Модель предпринимателя. При сохранении нового объекта данной модели происходит создание объекта в таблице-посреднике
    Suppliers2, которая нужна для того, чтобы объединить модели для поля supplier.
    """
    supplier = models.ForeignKey('chain.Suppliers1', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='долг перед поставщиком')

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


class Product(AbstractProduct):
    """
    Модель продукта
    """
    seller = models.ForeignKey('businessman', on_delete=models.CASCADE, verbose_name='предприниматель', **NULLABLE)
