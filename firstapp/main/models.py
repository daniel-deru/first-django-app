from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TodoListItems(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
