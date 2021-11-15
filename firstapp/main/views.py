from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, TodoListItems

def index(request):
    if request.method == "POST":
        todo = request.POST.get("todolist")
        if todo:
            todolist = TodoList(name=todo)
            todolist.save()
            redirect("index")
    todos = TodoList.objects.all()
    return render(request, "main/main.html", {"todos": todos})

def todos(request, todo_id):
    todo = TodoList.objects.get(id=todo_id)
    todoItems = TodoListItems.objects.filter(todolist=todo_id)
    
    if request.method == "POST":
        item = request.POST.get("item")
        todo.todolistitems_set.create(item=item)
    context = {
        "list": todo,
        "items": todoItems
    }
    return render(request, "main/todo.html", context)

def delete(request, item_id):
    todoitem = TodoListItems.objects.get(id=item_id)
    todoitem.delete()
    return redirect(request.META["HTTP_REFERER"])
