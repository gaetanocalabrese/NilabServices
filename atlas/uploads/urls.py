from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .core import views
from .core.views import DocumentDeleteView

urlpatterns = [

    path('simple/', views.simple_upload, name='simple_upload'),
    path('form/', views.model_form_upload, name='model_form_upload'),
    path('documents/', views.DocumentListView.as_view()),
    path('<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





