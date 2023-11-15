from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Organ, Host
from .permissions import IsHostAdmin


class HostAPI(APIView):
    permission_classes = [IsAuthenticated, IsHostAdmin]
    authentication_classes = [JWTAuthentication]

    class HostInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Host
            fields = ("name", "description")

        def create(self, validated_data):
            organ_id = self.context.get("organ_id")
            organ = get_object_or_404(Organ, id=organ_id)
            validated_data["organ"] = organ
            return super().create(validated_data)

    class HostOutputSerializer(serializers.Serializer):
        class Meta:
            model = Host
            fields = "__all__"

    def post(self, request, *args, **kwargs):
        organ_id = request.data.get("organ_id")
        
        # TODO: error handling for Organ instnace

        serializer = self.HostInputSerializer(
            data=request.data,
            context={"organ_id": organ_id},
        )
        if serializer.is_valid(raise_exception=True):
            host = serializer.save()
            json_to_return = self.HostOutputSerializer(host).data
            return Response(json_to_return, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
