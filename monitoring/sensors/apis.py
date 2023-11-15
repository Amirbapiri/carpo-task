from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.shortcuts import get_object_or_404

from .models import Department, Sensor


class SensorAPI(APIView):
    class SensorOutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Sensor
            fields = "__all__"

    def get(self, request, department_id=None, *args, **kwargs):
        
        if not department_id:
            return Response(
                {"error": "Department ID is a must"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            department_id = int(department_id)
        except ValueError:
            return Response(
                {"error": "Invalid department ID"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        department = get_object_or_404(Department, id=department_id)
        sensors = department.sensors.all()
        serializer = self.SensorOutputSerializer(sensors, many=True)

        return Response(serializer.data)
