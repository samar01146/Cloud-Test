from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Application, Environment, Instance, EnvironmentVariable
from .serializers import ApplicationSerializer, EnvironmentSerializer, InstanceSerializer, EnvironmentVariableSerializer, InstanceSerializerView

class ApplicationCreateView(APIView):
    def get(self, request, *args, **kwargs):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnvironmentCreateView(APIView):
    def get(self, request, *args, **kwargs):
        applications = Environment.objects.all()
        serializer = EnvironmentSerializer(applications, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = EnvironmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstanceCreateView(APIView):
    def get(self, request, *args, **kwargs):
        applications = Instance.objects.all()
        serializer = InstanceSerializerView(applications, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = InstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnvironmentVariableCreateView(APIView):
    def get(self, request, *args, **kwargs):
        applications = EnvironmentVariable.objects.all()
        serializer = EnvironmentVariableSerializer(applications, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = EnvironmentVariableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
