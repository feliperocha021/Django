from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .serializers import *
from .services import create_user_with_tokens

class CustomLoginView(TokenObtainPairView):
  serializer_class = TokenObtainPairSerializer
  
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    tokens = serializer.validated_data
    access = tokens.get("access")
    refresh = tokens.get("refresh")

    response = Response({"access": access})

    response.set_cookie(
      key="refresh_token",
      value=refresh,
      httponly=True,
      secure=True,
      samesite="Strict",
      max_age=60*60*24
    )

    return response

class SignupView(generics.CreateAPIView):
  serializer_class = SignupSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user, tokens = create_user_with_tokens(
      serializer.validated_data['username'],
      serializer.validated_data['email'],
      serializer.validated_data['password']
    )

    response = Response({
      "id": user.id,
      "username": user.username,
      "email": user.email,
      "access": tokens["access"]
    }, status=status.HTTP_201_CREATED)

    response.set_cookie(
      key="refresh_token",
      value=tokens["refresh"],
      httponly=True,
      secure=True,
      samesite="Strict",
      max_age=60*60*24
    )

    return response

class CustomRefreshView(APIView):
  def post(self, request, *args, **kwargs):
    refresh_token = request.COOKIES.get("refresh_token")
    if not refresh_token:
      return Response({"detail": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = TokenRefreshSerializer(data={"refresh": refresh_token})

    try:
      serializer.is_valid(raise_exception=True)
    except (InvalidToken, TokenError):
      return Response(
        {"detail": "Token is blacklisted or invalid"}, 
        status=status.HTTP_401_UNAUTHORIZED
      )
    
    data = serializer.validated_data
    access = data.get("access")
    new_refresh = data.get("refresh")

    response = Response({"access": access})
    if new_refresh:
      response.set_cookie(
        key="refresh_token",
        value=new_refresh,
        httponly=True,
        secure=True,
        samesite="Strict",
        max_age=60*60*24
      )

    return response

class MeView(generics.RetrieveAPIView):
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    return self.request.user
