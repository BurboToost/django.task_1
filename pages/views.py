from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Todo

# Create your views here.
def home(request):
    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Todo.objects.create(title=task)
        return redirect('home')

    tasks= Todo.objects.all().order_by('-id')
    return render(request, 'index.html',{
        'tasks':tasks
    })    
   

def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def delete_task (request, task_id):
    Todo.objects.filter(id= task_id).delete()
    return redirect('home')