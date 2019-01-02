from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from todo.models import Todos, TodoStatusTypes


def save_todo(todo_text: str, user: User, status: TodoStatusTypes):
    todo = Todos(
        todo_text=todo_text,
        user=user,
        status=status
    )
    todo.save()
    return todo


@login_required(login_url="todo:login")
@require_POST
def add_todo(request):
    data = dict(request.POST.items())
    todo_text = data['todo_text']
    status = TodoStatusTypes.objects.get_or_create(status_name='new')[0]
    save_todo(todo_text, request.user, status)
    return redirect('todo:index')


@login_required(login_url="todo:login")
def remove_todo(request, todo_id):
    todo = Todos.objects.get(pk=todo_id)
    status = TodoStatusTypes.objects.get_or_create(status_name='removed')[0]
    todo.status = status
    todo.save()
    return redirect("todo:index")
