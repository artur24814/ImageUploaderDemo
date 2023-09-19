from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions


class ListImages(APIView):
    """
    View to list all user's images in the system.

    * Requires token authentication.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all images.
        """
        images = [f'usdfuhdfhdsuf{image}' for image in range(10)]
        return Response(images)
