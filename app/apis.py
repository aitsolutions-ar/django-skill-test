from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from app.services import todo_create
from app.selectors import todo_list
from app.models import Todo


class TodoCreateApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        is_done = serializers.BooleanField(required=False,
                                           default=False)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        user_id = request.user.id
        serializer.is_valid(raise_exception=True)
        todo_create(user_id=user_id, **serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class TodoListApi(APIView):
    permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = (
                'id',
                'title',
                'description',
                'created_at',
                'is_done'
            )

    def get(self, request):
        todos = todo_list(user_id=request.user.id)
        data = self.OutputSerializer(todos, many=True).data
        return Response(data)