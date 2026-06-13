from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegistrationForm, TodoForm
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator  

def index(request):
    return render(request, 'todo/index.html')

def register(request) -> HttpResponse:
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else: # GET
        form = RegistrationForm()
    context = {"form": form}
    return render(request, template_name="todo/register.html", context=context)



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'todo/login.html', {'form': form})

def user_logout(request):
    logout(request)  
    return redirect('/') 


@login_required  
def todo_list(request):
    # Получаем все дела ТОЛЬКО текущего пользователя
    todos = Todo.objects.filter(owner=request.user)
    paginator = Paginator(todos, 1) 
    page_number = request.GET.get('page', 1)
    todos_page = paginator.get_page(page_number)
    return render(request, 'todo/todo_list.html', {'todos': todos_page})


@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            # Создаём объект, но не сохраняем в БД сразу
            todo = form.save(commit=False)
            # Подставляем текущего пользователя как владельца
            todo.owner = request.user
            todo.save()
            return redirect('todo_list')  
    form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

@ login_required
def todo_edit(request, todo_id):
    """Редактирование дела"""
    # Получаем дело по ID, проверяем что оно принадлежит текущему пользователю
    todo = get_object_or_404(Todo, id=todo_id, owner=request.user)
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()  
            return redirect('todo_list')  
    else:  # GET 
        form = TodoForm(instance=todo)  
    
    return render(request, 'todo/todo_edit.html', {'form': form, 'todo': todo})


@login_required
def todo_complete(request, todo_id):
    """Отметить дело как выполненное"""
    
    todo = Todo.objects.filter(id=todo_id, owner=request.user).first()
    
    if todo:  
        todo.is_completed = True
        todo.completed_at = timezone.now()  
        todo.save()
    
    return redirect('todo_list') 

@login_required
def todo_delete(request, todo_id):
    """Удаление дела с подтверждением"""
    todo = get_object_or_404(Todo, id=todo_id, owner=request.user)
    
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    
    # GET-запрос 
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})


