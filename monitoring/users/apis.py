from django.core.validators import MinLengthValidator

from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import SYSAdminUser, HostAdminUser
from .validators import number_validator, letter_validator, special_char_validator
from .services import register_sysadmin, register_hostadmin


class SysAdminRegistrationAPI(APIView):
    class InputSysAdminSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(
            max_length=100,
            validators=[
                number_validator,
                letter_validator,
                special_char_validator,
                MinLengthValidator(limit_value=8),
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

    def post(self, request, *args, **kwargs):
        serializer = self.InputSysAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = register_sysadmin(
                email=serializer.validated_data.get("email"),
                password=serializer.validated_data.get("password"),
            )
        except Exception as ex:
            return Response(
                f"Database error: {ex}",
                status=status.HTTP_400_BAD_REQUEST,
            )
        json_to_return = self.OutputSysAdminSerializer(
            user,
            context={"request": request},
        ).data
        return Response(
            json_to_return,
            status=status.HTTP_200_OK,
        )


class HostAdminRegistrationAPI(APIView):
    class InputHostAdminSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(
            max_length=100,
            validators=[
                number_validator,
                letter_validator,
                special_char_validator,
                MinLengthValidator(limit_value=8),
            ],
        )
        confirm_password = serializers.CharField(max_length=100)

        def validate_email(self, email):
            if HostAdminUser.objects.filter(email=email).exists():
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

    class OutputHostAdminSerializer(serializers.ModelSerializer):
        token = serializers.SerializerMethodField("get_token")

        class Meta:
            model = HostAdminUser
            fields = ("email", "token", "created_at", "updated_at")

        def get_token(self, user_instance):
            data = dict()

            token_class = RefreshToken

            refresh = token_class.for_user(user_instance)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return data

    def post(self, request, *args, **kwargs):
        serializer = self.InputHostAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = register_hostadmin(
                email=serializer.validated_data.get("email"),
                password=serializer.validated_data.get("password"),
            )
        except Exception as ex:
            return Response(
                f"Database error: {ex}",
                status=status.HTTP_400_BAD_REQUEST,
            )
        json_to_return = self.OutputHostAdminSerializer(
            user,
            context={"request": request},
        ).data
        return Response(
            json_to_return,
            status=status.HTTP_200_OK,
        )
