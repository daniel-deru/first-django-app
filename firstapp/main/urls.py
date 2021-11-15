from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo/<int:todo_id>', views.todos, name="todos"),
    path("delete/<int:item_id>", views.delete, name="delete")
]