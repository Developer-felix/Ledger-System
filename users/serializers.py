from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

        extra_kwargs = {
            "password": {"write_only": True},
        }

        def create(self, validated_data):
            user = User(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
            password = validated_data['password']
            password2 = validated_data['password2']
            if password != password2:
                raise serializers.ValidationError({'password': 'Passwords must match.'})
            user.set_password(password)
            user.save()
            return user


