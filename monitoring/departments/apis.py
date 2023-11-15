from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Department
from monitoring.hosts.models import Host
from .permissions import IsHostAdmin


class DepartmentAPI(APIView):
    permission_classes = [IsAuthenticated, IsHostAdmin]
    authentication_classes = [JWTAuthentication]

    class DepartmentInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Department
            fields = ("name", "host")

    class DepartmentOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Department
            fields = ("id", "name", "host")
            read_only_fields = ("id",)

    def post(self, request, *args, **kwargs):
        serializer = self.DepartmentInputSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            department = serializer.save()
            output_serializer = self.DepartmentOutputSerializer(department)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
