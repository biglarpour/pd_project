from django.db import models
from todo.models.todos import Todos, TodoStatusTypes
from todo.models.base import BaseModel


class TodoStatusHistory(BaseModel):
    todo_item = models.ForeignKey(Todos, on_delete=models.CASCADE, db_index=True)
    todo_status = models.ForeignKey(TodoStatusTypes, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        todo_text = (self.todo_item.todo_text[:30] + '..') if len(self.todo_item.todo_text) > 30 else self.todo_item.todo_text
        return f"{self.todo_item.user.username} {self.created_at} {todo_text} {self.todo_status.status_name}"

    class Meta:
        db_table = 'todo_status_history'
        app_label = 'todo'
        verbose_name = "Todo Status History"
        verbose_name_plural = "Todo Status Histories"
