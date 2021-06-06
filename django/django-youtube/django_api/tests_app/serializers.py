from .models import test_model
from rest_framework import serializers


class Simple_serializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    phone_number = serializers.IntegerField()
    is_alive = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)



    def create(self, validated_data):
        return test_model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        test_model.objects.filter(id=instance.id).update(**validated_data)
        return test_model.objects.get(id=instance.id)