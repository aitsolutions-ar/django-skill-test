from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import TodoSerializer
from .permissions import IsOwner
from .services import get_todo_by_id, get_todos_for_user, create_todo, update_todo, delete_todo

class TodoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def get(self, request):
        todos = get_todos_for_user(request.user)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(todos, request)
        serializer = TodoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            create_todo(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                is_done=serializer.validated_data['is_done'],
                user=request.user,
                deadline=serializer.validated_data.get('deadline')
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoRetrieveUpdateDeleteView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = TodoSerializer

    def get_object(self, pk):
        return get_todo_by_id(pk)

    def get(self, request, pk):
        todo = self.get_object(pk)
        if todo:
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        todo = self.get_object(pk)
        if todo:
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                update_todo(
                    todo,
                    title=serializer.validated_data.get('title'),
                    description=serializer.validated_data.get('description'),
                    is_done=serializer.validated_data.get('is_done'),
                    deadline=serializer.validated_data.get('deadline')
                )
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if todo:
            delete_todo(todo)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)