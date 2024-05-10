from rest_framework import status
from model_bakery import baker
import pytest
from store.models import Collection, Product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        product = baker.make(Product, description='description')

        response = api_client.post('/store/products/', product.__dict__)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, api_client, authenticate):
        authenticate()
        product = baker.make(Product, description='description')

        response = api_client.post('/store/products/', product.__dict__)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, api_client, authenticate):
        authenticate(is_staff=True)
        product = baker.make(Product,
                             title='',
                             description='',
                             slug='',
                             inventory=-1,
                             unit_price=-1)

        response = api_client.post('/store/products/', product.__dict__)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
        assert response.data['slug'] is not None
        assert response.data['inventory'] is not None
        assert response.data['unit_price'] is not None

    def test_if_data_is_valid_returns_201(self, api_client, authenticate):
        authenticate(is_staff=True)
        collection = baker.make(Collection)
        product_data = {
            'title': 'Test Product',
            'description': '',
            'slug': 'test-product',
            'inventory': 10,
            'unit_price': 10,
            'collection': collection.id
        }

        response = api_client.post('/store/products/', product_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'Test Product'
        assert response.data['description'] == ''
        assert response.data['slug'] == 'test-product'
        assert response.data['inventory'] == 10
        assert response.data['unit_price'] == 10
        assert response.data['collection'] == collection.id
