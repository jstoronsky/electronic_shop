from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Employee(AbstractUser):
    """
    модель пользователя
    """
    # ADMIN = 'admin'
    # USER = 'user'
    #
    # ROLE_CHOICES = [(ADMIN, 'Admin'), (USER, 'User')]
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    # role = models.CharField(max_length=15, choices=ROLE_CHOICES, verbose_name='права доступа', default=USER)
    image = models.ImageField(upload_to='users/', verbose_name='аватар пользователя', **NULLABLE)
    phone = models.CharField(max_length=15, verbose_name='номер телефона', **NULLABLE)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
