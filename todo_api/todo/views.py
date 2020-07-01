from rest_framework import generics

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.pk)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.pk)
