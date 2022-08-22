from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .permissions import IsOwnerOrAdmin
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, ClubCard, Feedback
from .serializers import (
    UserSerializer,
    ClubCardSerializer,
    FeedbackSerializer,
    LoginSerializer,
)


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "success",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class ClubCardViewSet(viewsets.ModelViewSet):
    serializer_class = ClubCardSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]

    def get_queryset(self):
        return ClubCard.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedBackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]

    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
