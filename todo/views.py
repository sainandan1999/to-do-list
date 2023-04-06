from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
    data=Todo.objects.all()
    if request.method=="POST":
        new_todo=Todo(title=request.POST['title'])
        new_todo.save()
        return redirect('/')
    contexts={'todos':data}
    return render(request,'index.html',contexts)

def delete(request,pk):
    delete_todo=Todo.objects.filter(id=pk)
    delete_todo.delete()
    return redirect('/')