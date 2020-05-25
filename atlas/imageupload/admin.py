from django.contrib import admin
from atlas.imageupload.models import UploadedImage

# Register the UploadedImage Model for the Admin Page
admin.site.register(UploadedImage)
