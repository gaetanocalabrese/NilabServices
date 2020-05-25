from django.conf.urls import url, include
from rest_framework import routers
from atlas.imageupload_rest.viewsets import UploadedImagesViewSet

# initiate router and register all endpoints
router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')
app_name = 'imageupload_rest'
# Wire up our API with our urls
urlpatterns = [
    url(r'^', include(router.urls)),
]
