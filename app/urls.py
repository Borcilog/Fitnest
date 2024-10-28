from django.urls import path
from .views import HomePageView, AboutPageView, BlogListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog')
]