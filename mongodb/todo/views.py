from django.shortcuts import render , redirect
from . models import Todo
from . forms import Todoforms
# Create your views here.
def todo(request):
    obj1=Todo.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        obj=Todo(headline=name)
        obj.save()
    return render(request,'todo.html',{'obj1':obj1})

def delete(request,todoid):
    todo=Todo.objects.get(id=todoid)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    return render(request,'delete.html',{'todo':todo})

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'todo':todo,'form':form})
