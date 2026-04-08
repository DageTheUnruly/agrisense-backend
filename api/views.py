from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorSerializer, UserSerializer
from rest_framework import status

@api_view(['GET'])
def get_sensors(request): # <--- Check this name
    data = SensorData.objects.all()
    serializer = SensorSerializer(data, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        return Response({
            "message": "Login successful", 
            "user": username,
            "status": "Authenticated"
        }, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)