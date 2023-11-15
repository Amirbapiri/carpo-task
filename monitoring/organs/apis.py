from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework import serializers

from .models import Organ



User = get_user_model()


class OrganAPI(APIView):
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
