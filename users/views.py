from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Payment, User
from .serializers import PaymentSerializer, UserRegisterSerializer, UserSerializer
from .services import create_checkout_session, create_price, create_product


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ["course", "lesson", "payment_method"]

    ordering_fields = ["payment_date"]


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        product = create_product(payment.course.title)

        price = create_price(product.id, payment.amount * 100)

        session = create_checkout_session(price.id)

        payment.stripe_session_id = session.id
        payment.payment_url = session.url
        payment.save()
