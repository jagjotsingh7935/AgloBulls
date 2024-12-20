from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
