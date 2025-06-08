from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import user

@api_view(['GET'])
def get_users(request):
    users = user.objects.all()
    serializer = UserSerializer(users,many = True)
    return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


