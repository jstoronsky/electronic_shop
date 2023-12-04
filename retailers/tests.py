from rest_framework.test import APITestCase
from rest_framework import status
from retailers.models import Retailer
from employers.models import Employee
# Create your tests here.


class RetailerTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_retailer(self):
        """
        тест создания ритейлера
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
            "/api/retailer/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Retailer.objects.all().count() > 0)

    def test_list_retailer(self):
        """
        тест вывода списка ритейлеров
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
        Retailer.objects.create(name="Завод завод", email="adasadssd@mail.bh", country="asdasdad", city="city",
                                street="dsadaadsasd", building=45, debt=0)
        response = self.client.get(
            '/api/retailer/',
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_retailer(self):
        """
        тест обновления ритейлера
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
        Retailer.objects.create(name="Завод завод", email="adasadssd@mail.bu", country="asdasdad", city="city",
                                street="dsadaadsasd", building=45, debt=0)

        data = {
            "city": "TFEWFWF",
        }

        response = self.client.patch(
            '/api/retailer/3/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/retailer/3/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Retailer.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        Employee.objects.all().delete()
        Retailer.objects.all().delete()
        return super().tearDown()
