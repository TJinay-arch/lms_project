from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PaymentListAPIView, RegisterAPIView, PaymentCreateAPIView

urlpatterns = [
    path("payments/", PaymentListAPIView.as_view()),
    path("payments/create/", PaymentCreateAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
