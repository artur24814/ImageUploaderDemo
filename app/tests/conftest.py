import pytest

from django.test import Client
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from imageuploader.models import (
    Profile, UserImage
)



@pytest.fixture
def client():
    return Client()


# Issue with file storage
@pytest.fixture
def in_memory():
    settings.DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    settings.FILE_UPLOAD_HANDLERS = ['django.core.files.uploadhandler.TemporaryFileUploadHandler',]


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def basic_user():
    return User.objects.create_user('User', password='user')

@pytest.fixture
def basic_users_image(basic_user):
    return UserImage.objects.create(profile=basic_user.profile, image='https://picsum.photos/200/300')


@pytest.fixture
def basic_users_image2(basic_user):
    return UserImage.objects.create(profile=basic_user.profile, image='https://picsum.photos/400/600')