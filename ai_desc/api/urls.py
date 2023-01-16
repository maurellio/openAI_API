from django.urls import path
from api.views import Generate, CreateUser, TestView


urlpatterns = [
    path('api/v1/generate', Generate.as_view(), name='generate'),
    path('api/v1/create_user', CreateUser.as_view(), name='create'),
    path('api/v1/test_view', TestView.as_view(), name='test'),
]