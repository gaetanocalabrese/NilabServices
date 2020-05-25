from django.conf.urls import include, url
from django.urls import path, include
from django.contrib import admin
from  atlas.tasks import views
from .views import JobTemplateView, LongTaskCreateView, Get_longTask_List
from django.contrib import admin


urlpatterns = [
    path('getLongTaskList/', views.getLongTaskList ,name = 'getLongTaskList'),
    path(r'^job/(?P<job>[\d\w-]+)/$', JobTemplateView.as_view()),
    path('long/', LongTaskCreateView.as_view(), name = 'long_tasks'),
]






 #   url(r'^home$', homepage),
   # path((r'^longtasksapi$', Get_longTask_List.as_view()),
  #  url(r'^$', TasksHomeFormView.as_view(), name='home'),
#


   # url(r'^admin/', admin.site.urls),
  #   url(r'^sendtoservice', JobPageView.as_view(), name='sendtoservice')


