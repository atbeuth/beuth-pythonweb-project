from django.urls import path
from .views import PostListView, PostDetailView
urlpatterns = [
 path('show', PostListView.as_view(), name='all-posts'),
 path('show/<int:pk>', PostDetailView.as_view(), name='postdetail'),

]
