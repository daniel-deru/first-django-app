from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, TodoListItems
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

def register(request):
    form = UserCreationForm()
    page = "register"
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            login(request, user)
    context = {
        "form": form,
        "page": page
    }
    return render(request, "main/login.html", context)

def loginPage(request):
    form = LoginForm()
    page = "login"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print("the login was unsuccessful")
    context = {
        "form": form,
        "page": page
    }
    return render(request, "main/login.html", context)

def index(request):
    if request.method == "POST":
        todo = request.POST.get("todolist")
        if todo:
            todolist = TodoList(name=todo)
            todolist.save()
            redirect("index")

    todos = TodoList.objects.all()
    return render(request, "main/main.html", {"todos": todos})

# This handles the click for the specific todo
def home(request, todo_id):
    delete_todo = TodoList.objects.get(id=todo_id)
    delete_todo.delete()
    return redirect('index')

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
