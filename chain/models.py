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
    objects = models.Manager()

    class Meta:
        abstract = True


class AbstractProduct(models.Model):
    name = models.CharField(max_length=35, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    release_date = models.DateTimeField(verbose_name='дата выхода продукта')
    objects = models.Manager()

    class Meta:
        abstract = True
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


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


class Suppliers1(models.Model):
    factory = models.OneToOneField('factory', on_delete=models.CASCADE, **NULLABLE)
    retailer = models.OneToOneField('retailers.retailer', on_delete=models.CASCADE, **NULLABLE)
    objects = models.Manager()

    def __str__(self):
        if self.factory is not None:
            return self.factory.name
        else:
            return self.retailer.name


class Suppliers2(models.Model):
    factory = models.OneToOneField('factory', on_delete=models.CASCADE, **NULLABLE)
    businessman = models.OneToOneField('businessmen.businessman', on_delete=models.CASCADE, **NULLABLE)
    objects = models.Manager()

    def __str__(self):
        if self.factory is not None:
            return self.factory.name
        else:
            return self.businessman.name


class Product(AbstractProduct):
    manufacturer = models.ForeignKey('factory', on_delete=models.CASCADE, verbose_name='производитель', **NULLABLE)
