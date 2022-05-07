from rest_framework import serializers
from .models import User


# User details serializer
class UserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Setting a minimal length validation for phone number
        if len(data['phone_number']) < 10:
            raise serializers.ValidationError("The phone number must contains min 10 digits.")
        return data

    class Meta:
        model = User
        fields = ('pk', 'firstname', 'lastname', 'email', 'phone_number', 'birthday_date')
