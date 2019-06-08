from django.urls import path
from . import views

from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
 path('show', PostListView.as_view(), name='all-posts'),
 path('show/<int:pk>', PostDetailView.as_view(), name='postdetail'),
 path('add', views.add_post, name='post-add'),
 path('success', success, name = 'success'), 
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
