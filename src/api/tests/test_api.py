from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT)
from rest_framework.test import APIClient

from shop.models import Category, Product


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10,
            category=self.category,
            active=True,
        )

        self.user = get_user_model()(
            email="test_api_user@localhost",
        )
        self.user.set_password("123456789")
        self.user.save()

    def test_product_details(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse("api:products_details", kwargs={"pk": self.product.pk}),
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_product_list(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse("api:products_list"),
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], self.product.name)

    def test_product_create(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            'name': 'Test Product 2',
            'description': 'Test description',
            'price': 10,
            'category': self.category.pk,
            'active': True,
        }

        response = self.client.post(reverse("api:products_create"), data=payload, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data['name'], payload['name'])

    def test_product_update(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            'price': 15,
        }

        response = self.client.patch(
            reverse("api:products_update", kwargs={"pk": self.product.pk}), data=payload, format='json'
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(float(response.data['price']), payload['price'])

    def test_product_delete(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse("api:products_delete", kwargs={"pk": self.product.pk}))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        response = self.client.get(
            reverse("api:products_details", kwargs={"pk": self.product.pk}),
        )
        self.assertTrue("name" not in response.data)
