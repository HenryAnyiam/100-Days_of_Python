from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Message


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().object.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', '')
        )
        return user

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    """serializer to handle user login"""

    email = serializers.EmailField()
    id = serializers.CharField(max_length=50, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        """validate login input"""

        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError("User Email is required for Login")
        
        if password is None:
            raise serializers.ValidationError("User Password is required for Login")
        
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")
        
        if not user.is_active:
            raise serializers.ValidationError("User is not active")

        return {"email": user.email, "id": user.id}

