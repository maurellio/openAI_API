from django.urls import path
from api.views import Generate


urlpatterns = [
    path('api/v1/generate', Generate.as_view(), name='generate')
]