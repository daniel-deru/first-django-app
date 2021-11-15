from django.contrib import admin

from .models import TodoList
from .models import TodoListItems

admin.site.register(TodoList)
admin.site.register(TodoListItems)
