from django.urls import path
from .views import ListImages


app_name = 'imageuploader'

urlpatterns = [
    path('', ListImages.as_view(), name='images'),
]
