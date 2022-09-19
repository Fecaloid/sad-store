from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        fields = (
            'username',
            'password',
        )


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)

    class Meta:
        fields = (
            'token',
        )
