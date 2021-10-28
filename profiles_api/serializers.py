from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer change data input to Python Object"""
    name = serializers.CharField(max_length=16)
