# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from employers.models import NULLABLE

# Create your models here.


class AbstractChain(models.Model):
    name = models.CharField(max_length=35, verbose_name='название')
    email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=20, verbose_name='страна')
    city = models.CharField(max_length=40, verbose_name='город')
    street = models.CharField(max_length=40, verbose_name='адрес')
    building = models.IntegerField(verbose_name='номер дома')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        abstract = True


class Factory(AbstractChain):
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Factory, self).save(*args, **kwargs)
        if not Suppliers1.objects.filter(factory=self).exists():
            sup_ = Suppliers1.objects.create(factory=self)
            sup_.save()
        if not Suppliers2.objects.filter(factory=self).exists():
            sup = Suppliers2.objects.create(factory=self)
            sup.save()

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Retailer(AbstractChain):
    # factory = models.ForeignKey('factory', on_delete=models.CASCADE,
    #                             verbose_name='поставщик(завод)', **NULLABLE)
    # individual = models.ForeignKey('individual_ent.Individual', on_delete=models.CASCADE,
    #                                verbose_name='поставщик(предприниматель)', **NULLABLE)
    # object_id = models.CharField(max_length=100, null=True, blank=True, verbose_name='id поставщика')
    # supplier_type = models.ForeignKey(
    #     ContentType, on_delete=models.CASCADE, null=True, blank=True,
    #     limit_choices_to=(models.Q(model__in=['factory', 'businessman'])), verbose_name='тип постащика')
    # supply = GenericForeignKey('supplier_type', 'object_id')
    supplier = models.ForeignKey('suppliers2', on_delete=models.CASCADE, verbose_name='поставщик(завод)', **NULLABLE)
    debt = models.FloatField(verbose_name='долг перед поставщиком')

    # supply.short_description = 'поставщик'

    def clean(self):
        for supplier in Suppliers2.objects.all():
            if self.supplier == supplier:
                if supplier.businessman is not None:
                    if supplier.businessman.supplier.retailer is not None and \
                            supplier.businessman.supplier.retailer.name == self.name:
                        raise ValidationError('You can not choose this supplier because you serve as supplier to it.')

    def save(self, *args, **kwargs):
        super(Retailer, self).save(*args, **kwargs)
        if not Suppliers1.objects.filter(retailer=self).exists():
            sup = Suppliers1.objects.create(retailer=self)
            sup.save()

    class Meta:
        verbose_name = 'ритейлер'
        verbose_name_plural = 'ритейлеры'


class Businessman(AbstractChain):
    supplier = models.ForeignKey('suppliers1', on_delete=models.CASCADE, verbose_name='поставщик(завод)', **NULLABLE)
    # individual = models.ForeignKey('individual_ent.Individual', on_delete=models.CASCADE,
    #                                verbose_name='поставщик(предприниматель)', **NULLABLE)
    debt = models.FloatField(verbose_name='долг перед поставщиком')
    objects = models.Manager()

    def clean(self):
        for supplier in Suppliers1.objects.all():
            if self.supplier == supplier:
                if supplier.retailer is not None:
                    if supplier.retailer.supplier.businessman is not None and \
                            supplier.retailer.supplier.businessman.name == self.name:
                        raise ValidationError('You can not choose this supplier because you serve as supplier to it.')

    def save(self, *args, **kwargs):
        super(Businessman, self).save(*args, **kwargs)
        if not Suppliers2.objects.filter(businessman=self).exists():
            sup = Suppliers2.objects.create(businessman=self)
            sup.save()

    class Meta:
        verbose_name = 'предприниматель'
        verbose_name_plural = 'предприниматели'


class Suppliers1(models.Model):
    factory = models.OneToOneField('factory', on_delete=models.CASCADE, **NULLABLE)
    retailer = models.OneToOneField('retailer', on_delete=models.CASCADE, **NULLABLE)
    objects = models.Manager()

    def __str__(self):
        if self.factory is not None:
            return self.factory.name
        else:
            return self.retailer.name


class Suppliers2(models.Model):
    factory = models.OneToOneField('factory', on_delete=models.CASCADE, **NULLABLE)
    businessman = models.OneToOneField('businessman', on_delete=models.CASCADE, **NULLABLE)
    objects = models.Manager()

    def __str__(self):
        if self.factory is not None:
            return self.factory.name
        else:
            return self.businessman.name


class Product(models.Model):
    name = models.CharField(max_length=35, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    manufacturer = models.ForeignKey('factory', on_delete=models.CASCADE, verbose_name='производитель')
    release_date = models.DateTimeField(verbose_name='дата выхода продукта')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
