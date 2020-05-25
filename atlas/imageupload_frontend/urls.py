from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.urls import path, include
# Redirect any request that goes into here to static/index.html
app_name = "imageupload_frontend"

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index')
]
