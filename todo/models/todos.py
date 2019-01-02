from django.contrib.auth.models import User
from django.db import models
from todo.models.base import BaseModel


class TodoStatusTypes(BaseModel):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = 'todo_status_types'
        app_label = 'todo'
        verbose_name = "Todo Status Type"
        verbose_name_plural = "Todo Status Types"


class Todos(BaseModel):
    todo_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    status = models.ForeignKey(TodoStatusTypes, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return f"{self.user.username} {self.todo_text}"

    class Meta:
        db_table = 'todos'
        app_label = 'todo'
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
