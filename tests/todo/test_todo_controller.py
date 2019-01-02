from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
from django.test import TestCase
from todo.models import Todos


class TestTodoController(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("email@email.com", "email@email.com", "MyV0!c3Is")

    def test_add_todo(self):
        client = Client()
        client.login(username="email@email.com", password="MyV0!c3Is")
        response = client.post(reverse('todo:add_todo'), {"todo_text": "my first todo item"})
        self.assertEqual(response.status_code, 302)
        todo = Todos.objects.get(user=self.user, todo_text="my first todo item")
        self.assertEqual(todo.status.status_name, 'new')

    def test_add_todo_missing_login(self):
        client = Client()
        response = client.post(reverse('todo:add_todo'), {"todo_text": "my first todo item"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/add_todo')

    def test_remove_todo(self):
        # create and confirm a todo exists
        client = Client()
        client.login(username="email@email.com", password="MyV0!c3Is")
        adds_todo = client.post(reverse('todo:add_todo'), {"todo_text": "my first todo item"})
        self.assertEqual(adds_todo.status_code, 302)
        todo = Todos.objects.get(user=self.user, todo_text="my first todo item")
        self.assertEqual(todo.status.status_name, 'new')

        # remove the todo using the remove_todo controller
        remove_todo = client.get(reverse('todo:remove_todo', kwargs={'todo_id': todo.id}))
        self.assertEqual(remove_todo.status_code, 302)
        todo = Todos.objects.get(user=self.user, todo_text="my first todo item")
        self.assertEqual(todo.status.status_name, 'removed')

    def test_remove_todo_missing_login(self):
        client = Client()
        response = client.post(reverse('todo:remove_todo', kwargs={'todo_id': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/1/remove_todo')
