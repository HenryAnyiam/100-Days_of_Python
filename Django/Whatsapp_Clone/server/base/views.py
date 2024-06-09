from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer, MessageSerializer
from .auth import UserAuthentication
from .models import Message

# Create your views here.

@api_view(['POST'])
def register_user(request):
    """register a new user"""

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """login a user"""

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token = UserAuthentication.encrypt_payload(payload=serializer.data)
        return Response({
            "message": "Login Successful",
            "token": token,
            "user": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_messages(request):
    """get all messages"""

    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

