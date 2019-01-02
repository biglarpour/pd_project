from django.contrib import admin
from todo.models import Todos, TodoStatusTypes, TodoStatusHistory

admin.site.register(Todos)
admin.site.register(TodoStatusTypes)
admin.site.register(TodoStatusHistory)
