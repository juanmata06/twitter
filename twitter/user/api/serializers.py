from rest_framework import serializers
from user.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'username', 'password']