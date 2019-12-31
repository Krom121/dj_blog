from django.urls import path
from .views import index, blog, post


urlpatterns = [
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<slug:slug>/<pk>/', post, name='post-detail'),
]
