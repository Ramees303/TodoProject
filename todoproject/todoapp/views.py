from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView,DeleteView

from todoapp.forms import TodoForm
from todoapp.models import Task

class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name ='task1'
class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']
    success_url=reverse_lazy('cbvhome')

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url=reverse_lazy('cbvhome')
def add(request):

    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    task1 = Task.objects.all()
    return  render(request,'home.html',{'task1':task1})



def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})










