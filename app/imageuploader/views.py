from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers, status

from .models import UserImage


class ListImages(APIView):
    """
    View to list all user's images in the system.

    * Requires token authentication.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    class ImageSeriaelizer(serializers.ModelSerializer):
        """
        Serializer for Patient model from patient_app

        Fields
        ------
        __all__: all model fields
        """
        class Meta:
            model = UserImage
            fields = ('image', )

    def get(self, request):
        """
        Return a list of all images.
        """
        images = UserImage.objects.filter(profile=request.user.profile)
        serializer = self.ImageSeriaelizer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Upload image
        """
        serializer = self.ImageSeriaelizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            profile_info = {'profile': request.user.profile}
            serializer.validated_data.update(profile_info)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
