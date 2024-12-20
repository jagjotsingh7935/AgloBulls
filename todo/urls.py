from django.urls import path
from django.views.generic import TemplateView
from .views import TodoCreateView, TodoListView, TodoDetailView



urlpatterns = [

     path('', TemplateView.as_view(template_name='todo/index.html'), name='home'),   

    path('api/todos/', TodoListView.as_view(), name='todo-list'),
    path('api/todos/create/', TodoCreateView.as_view(), name='todo-create'),
    path('api/todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),

    path('index/', TemplateView.as_view(template_name='todo/index.html'), name='index'),
]
