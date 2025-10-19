from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

def create_user_with_tokens(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()

    refresh = RefreshToken.for_user(user)
    return user, {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
