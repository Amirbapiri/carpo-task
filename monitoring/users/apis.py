from rest_framework.views import APIView
from rest_framework import serializers


from .models import SYSAdminUser


class SysAdminRegistrationAPI(APIView):
    class InputSysAdminSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(max_length=100,)
        confirm_password = serializers.CharField(max_length=100)

        def validate_email(self, email):
            if SYSAdminUser.objects.filter(email=email).exists():
                raise serializers.ValidationError("Email's already taken")
            return email

        def validate(self, data):
            if not data.get("password") or not data.get("confirm_password"):
                raise serializers.ValidationError(
                    "Please fill password and confirm password"
                )

            if data.get("password") != data.get("confirm_password"):
                raise serializers.ValidationError(
                    "confirm password is not equal to password"
                )
            return data
