from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import TodoSerializer
from .permissions import IsOwner
from .services import get_todo_by_id, get_todos_for_user, create_todo, update_todo, delete_todo

class TodoListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        todos = get_todos_for_user(request.user)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(todos, request)
        serializer = TodoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            create_todo(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                user=request.user,
                deadline=serializer.validated_data.get('deadline')
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)