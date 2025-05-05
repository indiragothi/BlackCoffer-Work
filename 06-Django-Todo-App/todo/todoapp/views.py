 

# Create your views here.
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import TodoForm

def todo_list(request):
    # Initialize todos list in session if it doesn't exist
    if 'todos' not in request.session:
        request.session['todos'] = []
    
    todos = request.session['todos']
    return render(request, 'todoapp/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = {
                'id': len(request.session.get('todos', [])),
                'title': form.cleaned_data['title'],
                'description': form.cleaned_data['description'],
                'completed': form.cleaned_data['completed']
            }
            
            # Get the todos list from session
            todos = request.session.get('todos', [])
            todos.append(todo)
            
            # Update the session
            request.session['todos'] = todos
            
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    return render(request, 'todoapp/todo_form.html', {'form': form, 'action': 'Create'})

def todo_update(request, todo_id):
    # Get the todos list from session
    todos = request.session.get('todos', [])
    
    # Find the todo by id
    todo = None
    for item in todos:
        if item['id'] == todo_id:
            todo = item
            break
    
    if todo is None:
        raise Http404("Todo does not exist")
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # Update the todo
            todo['title'] = form.cleaned_data['title']
            todo['description'] = form.cleaned_data['description']
            todo['completed'] = form.cleaned_data['completed']
            
            # Update the session
            request.session['todos'] = todos
            
            return redirect('todo_list')
    else:
        form = TodoForm(initial=todo)
    
    return render(request, 'todoapp/todo_form.html', {'form': form, 'action': 'Update'})

def todo_delete(request, todo_id):
    # Get the todos list from session
    todos = request.session.get('todos', [])
    
    # Find the todo by id and remove it
    updated_todos = []
    for item in todos:
        if item['id'] != todo_id:
            updated_todos.append(item)
    
    # Update the session
    request.session['todos'] = updated_todos
    
    return redirect('todo_list')