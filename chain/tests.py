from rest_framework.test import APITestCase
from rest_framework import status
from chain.models import Factory, Product
from employers.models import Employee
# Create your tests here.


class FactoryTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_factory(self):
        """
        тест создания объекта завода
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
            "building": 45
        }
        response = self.client.post(
            "/api/factory/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Factory.objects.all().count() > 0)

    def test_list_factory(self):
        """
        тест вывода списка заводов
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
        Factory.objects.create(name="Завод завод", email="adasadssd@mail.bh", country="asdasdad", city="city",
                               street="dsadaadsasd", building=45)
        response = self.client.get(
            '/api/factory/',
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_factory(self):
        """
        тест обновления завода
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
        Factory.objects.create(name="Завод завод", email="adasadssd@mail.bu", country="asdasdad", city="city",
                               street="dsadaadsasd", building=45)

        data = {
            "city": "TFEWFWF",
        }

        response = self.client.patch(
            '/api/factory/3/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/factory/3/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Factory.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        Employee.objects.all().delete()
        Factory.objects.all().delete()
        return super().tearDown()


class ProductTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_product(self):
        """
        тест создания продукта
        """
        user = Employee.objects.create(email='dada@test.com', is_active=True)
        user.set_password('edcrfvtgb')
        user.save()
        data1 = {
            "email": "dada@test.com",
            "password": "edcrfvtgb"
        }
        user_response = self.client.post(
            "/employers/login/",
            data=data1
        )
        token = user_response.data['access']

        factory = Factory.objects.create(name="Завод завод", email="adasadssd@mail.bu", country="asdasdad", city="city",
                                         street="dsadaadsasd", building=45)
        data = {
            "name": "Завод завод",
            "model": "adasadssczxxc2eqwesa",
            "manufacturer": factory.id
        }
        response = self.client.post(
            "/api/product_factory/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Product.objects.all().count() > 0)

    def test_list_product(self):
        """
        тест вывода списка продуктов
        """
        user = Employee.objects.create(email='sutulaya_sobaka@test.com', is_active=True)
        user.set_password('wdzxczxyty')
        user.save()
        data1 = {
            "email": "sutulaya_sobaka@test.com",
            "password": "wdzxczxyty"
        }
        user_response = self.client.post(
            "/employers/login/",
            data=data1
        )
        token = user_response.data['access']
        factory = Factory.objects.create(name="Завод завод", email="adasadssd@mail.bu", country="asdasdad", city="city",
                                         street="dsadaadsasd", building=45)
        Product.objects.create(name="Завод завод", model="adasadssczxxc2eqwesa", manufacturer=factory)
        response = self.client.get(
            '/api/product_factory/',
            headers={"Authorization": f"Bearer {token}"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """
        тест обновления продукта
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
        factory = Factory.objects.create(name="Завод завод", email="adasadssd@mail.bu", country="asdasdad", city="city",
                                         street="dsadaadsasd", building=45)
        Product.objects.create(name="Завод завод", model="adasadssczxxc2eqwesa", manufacturer=factory)

        data = {
            "model": "TFEWFWFasda23qeq"
        }

        response = self.client.patch(
            '/api/product_factory/3/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/product_factory/3/',
            headers={"Authorization": f"Bearer {token}"}
        )
        queryset = Product.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        Employee.objects.all().delete()
        Factory.objects.all().delete()
        Product.objects.all().delete()
        return super().tearDown()
