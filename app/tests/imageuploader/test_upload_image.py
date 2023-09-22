import pytest
import json
import datetime
import io
import os
import shutil
from PIL import Image
import tempfile

from django.urls import reverse
from rest_framework.authtoken.models import Token


def generate_photo_file():
    file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file


@pytest.mark.django_db
def test_image_upload_forbidden(api_client, basic_user):
    response = api_client.post(reverse('imageuploader:images'), data={'image': generate_photo_file()})

    assert response.status_code == 401


@pytest.mark.django_db
def test_test_image_list(api_client, basic_user):

    token = Token.objects.get(user=basic_user)

    headers = {"Authorization": f"Token {token.key}"}
    response = api_client.post(reverse('imageuploader:images'), headers=headers, data={'image': generate_photo_file()})

    assert response.status_code == 200
    responce_data = json.loads(json.dumps(response.data))
    assert responce_data['image'] is not None

    # delete media repo
    directory = os.getcwd()
    if directory.split('\\')[-1] == 'tests':
        shutil.rmtree('media')