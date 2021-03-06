from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers


class GetUsers(APIView):
    def get(self, request, format=None):
        all_users = models.User.objects.all()
        serializer = serializers.UserSerializer(all_users, many=True)
        return Response(serializer.data)

class GetUserById(APIView):
    def post(self, request, format=None):
        _id = request.POST.get("id")
        user = models.User.objects.filter(pk=_id)
        serializer = serializers.UserSerializer(user, many=True)
        return Response(serializer.data)

