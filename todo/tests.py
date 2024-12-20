from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Todo

class TodoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_data = {
            "title": "Test Task",
            "description": "This is a test description.",
            "status": "OPEN",
        }
        self.todo = Todo.objects.create(**self.todo_data)

    def test_create_todo(self):
        response = self.client.post(reverse('todo-create'), self.todo_data)
        self.assertEqual(response.status_code, 201)

    def test_list_todos(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)

    def test_retrieve_todo(self):
        response = self.client.get(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, 200)

    def test_update_todo(self):
        response = self.client.put(reverse('todo-detail', kwargs={'pk': self.todo.id}),
                                   {"title": "Updated Task", "description": "Updated description.", "status": "WORKING"})
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        response = self.client.delete(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, 204)
