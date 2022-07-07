from django.db import router
from django.urls import path, include
from rest_framework import routers

from .views import UserDetailAPI,RegisterUserAPIView, LoginView
router = routers.DefaultRouter()



urlpatterns = [
  path('api', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path("get-details/",UserDetailAPI.as_view()),
  path('api/signup/',RegisterUserAPIView.as_view()),
  path('api/login/', LoginView.as_view()),

]