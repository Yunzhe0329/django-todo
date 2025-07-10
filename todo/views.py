from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo_list')
        else:
            return render(request, 'todo/login.html', {'error': '登入失敗'})
    return render(request, 'todo/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    form = TodoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        new_todo = form.save(commit=False)
        new_todo.user = request.user  # ← 設定 user 欄位
        new_todo.save()
        return redirect('todo_list')

    return render(request, 'todo/todo_list.html', {'form': form, 'todos': todos})

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.user == request.user:
        todo.delete()
    return redirect('todo_list')

@login_required
def toggle_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.user == request.user:
        todo.completed = not todo.completed
        todo.save()
    return redirect('todo_list')

