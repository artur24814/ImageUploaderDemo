import pytest
import json
from django.urls import reverse
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_image_list_forbidden(api_client, basic_user):
    response = api_client.get(reverse('imageuploader:images'))

    assert response.status_code == 401


@pytest.mark.django_db
def test_test_image_list(api_client, basic_user, basic_users_image, basic_users_image2):

    token = Token.objects.get(user=basic_user)

    headers = {"Authorization": f"Token {token.key}"}
    response = api_client.get(reverse('imageuploader:images'), headers=headers)

    assert response.status_code == 200
    responce_data = json.loads(json.dumps(response.data))
    assert len(responce_data) == 2
    assert responce_data[0]['image'] == '/media/https%3A/picsum.photos/200/300'
    assert responce_data[1]['image'] == '/media/https%3A/picsum.photos/400/600'

