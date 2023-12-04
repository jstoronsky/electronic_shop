from django.core.management import BaseCommand

from employers.models import Employee


class Command(BaseCommand):
    def handle(self, *args, **options):
        superuser = Employee.objects.create(
            email='jstoronsky@testt.com',
            first_name='Admin',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        superuser.set_password('Demon6600')
        superuser.save()
