from django.shortcuts import render, redirect
from . forms import TaskForm
from . models import AddTask
from datetime import datetime

# Create your views here.
def AddTaskForm(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtask')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def ShowInCompleteTask(request):
    task = AddTask.objects.filter(status='INCOMPLETE')
    return render(request, 'show_task.html', {'task': task})

def ShowCompleteTask(request):
    task = AddTask.objects.filter(status='COMPLETE')
    return render(request, 'complete_task.html', {'task': task})

def CompleteTask(request, id):
    task = AddTask.objects.get(pk=id)
    task.status = 'COMPLETE'
    task.save()
    return redirect('showtask')

def EditTask(request,id):
    task = AddTask.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.last_update = datetime.now()
            task.edit_cnt += 1
            form.save()
            return redirect('showtask')
    return render(request, 'add_task.html', {'form': form})

def DetailTask(request,id):
    task = AddTask.objects.get(pk=id)
    return render(request, 'detail.html', {'task': task})

def DeleteTask(request,id):
    AddTask.objects.get(pk=id).delete()
    return redirect('showtask')