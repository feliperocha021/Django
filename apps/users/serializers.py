from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import User

class SignupSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True}}

  def validate_password(self, value):
    try:
      validate_password(value)
    except DjangoValidationError as e:
      raise serializers.ValidationError(e.messages)
    return value

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'date_joined',
        'last_login',
    ]
    read_only_fields = ['id', 'date_joined', 'last_login']

