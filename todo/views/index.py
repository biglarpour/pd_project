from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from todo.models import Todos


@login_required(login_url="todo:login")
def index(request):
    user_todos = Todos.objects.filter(user__id=request.user.id).exclude(status__status_name="removed").order_by('created_at')
    return render(request, 'index.html', {'todos': user_todos})
