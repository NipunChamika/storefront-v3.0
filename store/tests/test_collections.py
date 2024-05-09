from rest_framework import status
import pytest
from model_bakery import baker
from store.models import Collection


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.fixture
def update_collection(api_client):
    def do_update_collection(title, collection):
        return api_client.put(f'/store/collections/{collection.id}/', title)
    return do_update_collection


@pytest.fixture
def delete_collection(api_client):
    def do_delete_collection():
        collection = baker.make(Collection)
        return api_client.delete(f'/store/collections/{collection.id}/')
    return do_delete_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        # Arrange

        # Act
        response = create_collection({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_collection, authenticate):
        # Arrange
        authenticate()

        # Act
        response = create_collection({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_collection, authenticate):
        # Arrange
        authenticate(is_staff=True)

        # Act
        response = create_collection({'title': ''})

        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, create_collection, authenticate):
        # Arrange
        authenticate(is_staff=True)

        # Act
        response = create_collection({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_does_not_exist_returns_404(self, api_client):
        non_existent_id = 9999999

        response = api_client.get(f'/store/collections/{non_existent_id}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_collection_exists_returns_200(self, api_client):
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }


@pytest.mark.django_db
class TestUpdateCollection:
    def test_if_user_is_anonymous_returns_401(self, update_collection):
        collection = baker.make(Collection)

        response = update_collection({'title': 'a'}, collection)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, update_collection, authenticate):
        authenticate()
        collection = baker.make(Collection)

        response = update_collection({'title': 'a'}, collection)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, update_collection, authenticate):
        authenticate(is_staff=True)
        collection = baker.make(Collection)

        response = update_collection({'title': ''}, collection)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_200(self, update_collection, authenticate):
        authenticate(is_staff=True)
        collection = baker.make(Collection)

        response = response = update_collection({'title': 'a'}, collection)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': 'a',
            'products_count': 0
        }


@pytest.mark.django_db
class TestDeleteCollection:
    def test_if_user_is_anonymous_returns_401(self, delete_collection):
        response = delete_collection()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, delete_collection, authenticate):
        authenticate()
        response = delete_collection()

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_collection_deletes_returns_204(self, delete_collection, authenticate):
        authenticate(is_staff=True)
        response = delete_collection()

        assert response.status_code == status.HTTP_204_NO_CONTENT
