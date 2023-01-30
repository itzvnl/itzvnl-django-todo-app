from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST
import datetime



# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    date = datetime.datetime.now()
    print(date)
    form = TodoForm()
    context = {'todo_list': todo_list,'form':form,'date': date}
    return render(request,'todo/index.html',context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    
    print(request.POST['text'])

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')




def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
