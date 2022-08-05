from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task1'
    fields = ('name', 'work', 'date')

    def get_success_url(self):
        return reverse_lazy('cvbdetail', kwargs={'pk':self.object.id})

# Create your views here.
def hello(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name',)
        work=request.POST.get('work',)
        date=request.POST.get('date',)
        task=Task(name=name,work=work,date=date)
        task.save()

    return render(request,'index.html',{'task1':task1})
def delete(request,taskid):
    tast2=Task.objects.get(id=taskid)
    if request.method=='POST':
        tast2.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'edit.html',{'f':f,'task':task})