from rest_framework import serializers
from .models import Application, Environment, Instance, EnvironmentVariable

class EnvironmentVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentVariable
        fields = '__all__'

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = '__all__'
    
    
class InstanceSerializerView(serializers.ModelSerializer):
    environment = serializers.SerializerMethodField(required=False)
    def get_environment(self, obj):
        if not obj.environment:
            return None
        return {
            "id": obj.environment.id,
            "name": obj.environment.name,
        }
    class Meta:
        model = Instance
        fields = '__all__'
    
    

class EnvironmentSerializer(serializers.ModelSerializer):
    variables = EnvironmentVariableSerializer(many=True, required=False)
    instances = InstanceSerializer(many=True, required=False)

    class Meta:
        model = Environment
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    environments = EnvironmentSerializer(many=True, required=False)

    class Meta:
        model = Application
        fields = '__all__'
