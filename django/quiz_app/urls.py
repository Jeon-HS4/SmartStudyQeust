from django.urls import path
from . import views

urlpatterns = [
    path('api/crawl/', views.crawl_api, name='crawl_api'),
]