from django.urls import path
from .views import index, blog, post


urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('post/', post),
]
