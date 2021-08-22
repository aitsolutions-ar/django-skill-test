from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from api_helpers.mixins import ApiErrorsMixin

from rest_framework.permissions import IsAuthenticated

from app.services import todo_create, todo_markasdone, todo_delete
from app.selectors import todo_list, todo_get
from app.models import Todo

from api_helpers.pagination import get_paginated_response, LimitOffsetPagination


class TodoListApi(APIView):
    permission_classes = [IsAuthenticated]

    class Pagination(LimitOffsetPagination):
        default_limit = 2

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = (
                'id',
                'title',
                'description',
                'created_at',
                'is_done',
                'completion_deadline'
            )

    def get(self, request):
        todos = todo_list(user_id=request.user.id)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=todos,
            request=request,
            view=self
        )


class TodoCreateApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        is_done = serializers.BooleanField(required=False,
                                           default=False)
        completion_deadline = serializers.DateTimeField(required=False,
                                                        default=None)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        user_id = request.user.id
        serializer.is_valid(raise_exception=True)
        todo_create(user_id=user_id, **serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class TodoDetailApi(APIView, ApiErrorsMixin):
    permission_classes = [IsAuthenticated]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = (
                'id',
                'title',
                'description',
                'created_at',
                'is_done',
                'completion_deadline'
            )

    def get(self, request, todo_id):
        todo = todo_get(fetched_by=request.user, todo_id=todo_id)
        serializer = self.OutputSerializer(todo)
        return Response(serializer.data)


class TodoUpdateApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        is_done = serializers.BooleanField()

    def post(self, request, todo_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo_markasdone(fetched_by=request.user, todo_id=todo_id, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class TodoDeleteApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todo_id):
        todo_delete(fetched_by=request.user, todo_id=todo_id)
        return Response(status=status.HTTP_200_OK)
