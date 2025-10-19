from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import SignupView, MeView, CustomLoginView, CustomRefreshView

urlpatterns = [
  path('signup/', SignupView.as_view(), name='signup'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('refresh-token/', CustomRefreshView.as_view(), name='signup'),
  path('me/', MeView.as_view(), name='me'),
]