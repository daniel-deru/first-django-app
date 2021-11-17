from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.home, name="home"),
    path('todo/<int:todo_id>', views.todos, name="todos"),
    path("delete/<int:item_id>", views.delete, name="delete")
]