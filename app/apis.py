from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from app.services import todo_create


class TodoCreateApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        is_done = serializers.BooleanField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        user_id = request.user.id
        serializer.is_valid(raise_exception=True)
        todo_create(user_id=user_id, **serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)