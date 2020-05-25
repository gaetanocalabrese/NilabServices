from rest_framework import viewsets, filters
from atlas.imageupload_rest.serializers import UploadedImageSerializer
from atlas.imageupload.models import UploadedImage


# ViewSet for our UploadedImage Model
# Gets all images from database and serializes them using UploadedImageSerializer
class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

