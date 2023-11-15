from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import SYSAdminUser
from .validators import number_validator, letter_validator, special_char_validator


class SysAdminRegistrationAPI(APIView):
    class InputSysAdminSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(
            max_length=100,
            validators=[
                number_validator,
                letter_validator,
                special_char_validator,
            ],
        )
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

    class OutputSysAdminSerializer(serializers.ModelSerializer):
        token = serializers.SerializerMethodField("get_token")

        class Meta:
            model = SYSAdminUser
            fields = ("email", "token", "created_at", "updated_at")

        def get_token(self, user_instance):
            data = dict()

            token_class = RefreshToken

            refresh = token_class.for_user(user_instance)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return data
