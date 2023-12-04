from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

v1_router = DefaultRouter()
v1_router.register('books', BookViewSet, basename='books')


urlpatterns = [
    path('v1/', v1_router.urls),
]