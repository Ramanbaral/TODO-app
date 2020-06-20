from django.shortcuts import render,redirect
from TODO_with_DB.models import task

# Create your views here.
def index(request):
    if request.method=='POST':
        title=request.POST.get('textarea')
        print(title)
        todo=task(title=title)
        todo.save()
    #getting tasks which  are not completed
    pending_task=task.objects.filter(completed=False)
    l=len(pending_task)
    #getting all tasks from our database to display in index
    tasks=task.objects.all()
    params={'tasks':tasks,'l':l}

    return render(request,'index.html',params)

def edit(request,pk):
    todo_task=task.objects.get(id=pk)
    if request.method=='POST':
        new_task=request.POST.get('newtask',todo_task.title)  
        if new_task=="":
            new_task=todo_task.title
        status=request.POST.get('status','off')
        print(status)
        if status=='on':
            todo_task.completed=True
        else:
            todo_task.completed=False

        print(todo_task.completed)
        print(new_task)
        todo_task.title=new_task
        todo_task.save()
        return redirect('/')

    status=task.objects.get(id=pk).completed
    return render(request,'edit.html',{'pk':pk,'todo_task':todo_task,'status':status})

def delete(request,pk):
    # getting the objects
    todo_task=task.objects.get(id=pk)
    # deleting the object
    todo_task.delete()
    # by taking the id from pk i will delete the task and dispaly delete message and redirect the user to home page
    return redirect('/')
