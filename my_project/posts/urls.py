from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
 path('show', PostListView.as_view(), name='all-posts'),
 path('show/<int:pk>', PostDetailView.as_view(), name='postdetail'),
 path('add', views.add_post, name='post-add'),
]
