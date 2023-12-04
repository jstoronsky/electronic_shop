from rest_framework.test import APITestCase
from rest_framework import status
from businessmen.models import Businessman
from employers.models import Employee
# Create your tests here.


class BusinessmenTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_businessman(self):
        """
        тест создания предпринимателя
        """
        user = Employee.objects.create(email='duck@test.com', is_active=True)
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "duck@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/employers/login/",
            data=data1
        )
        token = user_response.data['access']
        data = {
            "name": "Завод завод",
            "email": "adasadssd@mail.bg",
            "country": "asdasdad",
            "city": "city",
            "street": "dsadaadsasd",
            "building": 45,
            "debt": 0
        }
        response = self.client.post(
            "/api/businessman/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Businessman.objects.all().count() > 0)

    def test_list_businessman(self):
        """
        тест вывода списка предпринимателей
        """
        user = Employee.objects.create(email='dadad@test.com', is_active=True)
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": 'dadad@test.com',
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/employers/login/",
            data=data1
        )
        token = user_response.data['access']
        Businessman.objects.create(name="Завод завод", email="adasadssd@mail.bh", country="asdasdad", city="city",
                                   street="dsadaadsasd", building=45, debt=0)
        response = self.client.get(
            '/api/businessman/',
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_businessman(self):
        """
        тест обновления предпринимателя
        """
        user = Employee.objects.create(email='dadada@test.com', is_active=True)
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "dadada@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/employers/login/",
            data=data1
        )
        token = user_response.data['access']
        Businessman.objects.create(name="Завод завод", email="adasadssd@mail.bu", country="asdasdad", city="city",
                                   street="dsadaadsasd", building=45, debt=0)

        data = {
            "city": "TFEWFWF",
        }

        response = self.client.patch(
            '/api/businessman/3/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/businessman/3/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Businessman.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        Employee.objects.all().delete()
        Businessman.objects.all().delete()
        return super().tearDown()
