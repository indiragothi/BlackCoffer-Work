# Django Todo Application

A simple Django web application for managing your todo items. This app allows users to create, read, update, and delete todo items without using a database, storing data in sessions instead.

## Features

- Create new todo items
- View list of all todo items
- Update existing todo items
- Delete todo items
- No database required (uses session storage)
- Simple and clean UI
- CRUD operations (Create, Read, Update, Delete)

## Project Structure

```
todo/
├── manage.py                 # Django command-line utility
├── todo/                     # Main Django project
│   ├── __init__.py
│   ├── asgi.py               # ASGI config
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI config
│
├── todoapp/                  # Django app
│   ├── __init__.py
│   ├── admin.py              # Admin configurations
│   ├── apps.py               # App configuration
│   ├── forms.py              # Form definitions
│   ├── models.py             # Data models (empty in this case)
│   ├── tests.py              # Tests
│   ├── urls.py               # App URL configurations
│   ├── views.py              # View functions
│   └── templates/            # HTML templates
│       └── todoapp/
│           ├── base.html     # Base template
│           ├── todo_list.html # Todo listing page
│           └── todo_form.html # Create/update form
```

## Setup Instructions

### 1. Clone the repository or create the project structure as shown above

### 2. Install Python 3.12
Download and install Python from [python.org](https://www.python.org/downloads/) or use your package manager.

### 3. Set up a virtual environment using Conda
```bash
# Create a new conda environment
conda create -n venv python==3.12 -y
# Activate the environment
conda activate venv
```

### 4. Create directory
```bash
mkdir todo
cd todo
```

### 5. Install Django
```bash
pip install django
```

### 6. Create Django project
```bash
python -m django startproject todo .
```

### 7. Create Django app
```bash
python manage.py startapp todoapp
```

### 8. Run the migrations
```bash
python manage.py migrate
```

### 9. Run the development server
```bash
python manage.py runserver
```

### 10. Access the application
Open your web browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## How It Works

1. The app initializes a Django web server
2. When a user accesses the homepage, they see a list of all todo items (if any exist)
3. Users can add new todo items by clicking the "Add New Todo" button
4. Each todo item can be edited or deleted using the action buttons
5. Todo items are stored in the Django session, so they persist between page loads but will be cleared when the session expires

## Django Documentation

For more information about Django:
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)