from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
from .serializer import UserGetSerializer

User = get_user_model()

# Create your views here.

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_list(request):
    """get all users"""

    try:
        users = User.object.exclude(id=request.user.id)
        serializer = UserGetSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print("Error in getting users list", str(e))
        return Response({"error": "Error in getting users list"}, status=status.HTTP_400_BAD_REQUEST)
