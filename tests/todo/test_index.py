from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
from django.test import TestCase
from todo.models import Todos, TodoStatusTypes


class TestIndex(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("email@email.com", "email@email.com", "MyV0!c3Is")
        self.todo = Todos(user=self.user, status=TodoStatusTypes.objects.get_or_create(status_name='new')[0],
                          todo_text="my first todo item")
        self.todo.save()

    def test_index_with_todo(self):
        self.client.login(username="email@email.com", password="MyV0!c3Is")
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('my first todo item', str(response.content))

    def test_index_missing_login(self):
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', str(response.url))
