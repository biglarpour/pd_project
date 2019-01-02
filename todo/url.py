from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from todo.controllers.todo_controller import add_todo, remove_todo
from todo.views.index import index
from todo.views.signup import signup

app_name = 'todo'
urlpatterns = [
    path('', index, name='index'),
    path('add_todo', add_todo, name='add_todo'),
    path('<todo_id>/remove_todo', remove_todo, name='remove_todo'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='todo:login'), name='logout')
]