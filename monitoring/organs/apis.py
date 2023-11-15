from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Organ
from .permissions import IsSysAdmin, IsHostAdmin


User = get_user_model()


class OrganAPI(APIView):
    permission_classes = [IsAuthenticated, IsSysAdmin]
    authentication_classes = [JWTAuthentication]
    
    class OrganSysAdminOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("email",)

    class OrganInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Organ
            fields = (
                "name",
                "description",
            )

    class OrganOutputSerializer(serializers.ModelSerializer):
        sys_admin = serializers.SerializerMethodField()

        class Meta:
            model = Organ
            fields = ("name", "description", "sys_admin")

        def get_sys_admin(self, organ_instance):
            return organ_instance.sys_admin.email

    def post(self, request, *args, **kwargs):
        serializer = self.OrganInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            organ = serializer.save(sys_admin=request.user)
        except Exception as ex:
            return Response(
                f"Database error: {ex}",
                status=status.HTTP_400_BAD_REQUEST,
            )
        json_to_return = self.OrganOutputSerializer(organ).data
        return Response(
            json_to_return,
            status=status.HTTP_201_CREATED,
        )
