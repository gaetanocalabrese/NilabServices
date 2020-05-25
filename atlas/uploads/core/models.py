from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from users.models import CustomUser

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)

    feature_image = models.ImageField(upload_to='tutorial/images/')

    titolo = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(CustomUser,
        null=True, blank=True, on_delete=models.SET_NULL)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)
