from django.urls import path
from .views import index, blog, post


urlpatterns = [
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<pk>/', post, name='post-detail'),
]
