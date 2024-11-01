from django.urls import path
from . import views
from .views import (HomePageView, AboutPageView, BlogListView,
                     BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, ContactPageView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('Video/Upload', views.upload_video, name='Video'),
    path('Videos/',views.video_list, name='Video_list'),
    path('Contact/', ContactPageView.as_view(), name='Contact'),
]
