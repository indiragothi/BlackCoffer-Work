# Django Quote Generator

A simple Django web application that displays random motivational quotes. The app fetches quotes from an external API and provides fallbacks when the API is unavailable.

## Features

- Random motivational quotes display
- New quote on button click without page refresh
- Fallback quotes when API is unavailable
- Simple and clean UI

## Project Structure

```
Storefront/
│
├── manage.py                 # Django command-line utility
├── storefront/               # Main Django project
│   ├── __init__.py
│   ├── asgi.py               # ASGI config
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI config
│
├── quotes/                   # Django app
│   ├── __init__.py
│   ├── admin.py              # Admin configurations
│   ├── apps.py               # App configuration
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py             # Data models
│   ├── services.py           # Service for fetching quotes
│   ├── tests.py              # Tests
│   ├── urls.py               # App URL configurations
│   └── views.py              # View functions
│
├── static/                   # Static files (CSS, JS)
│   └── css/
│       └── style.css
│
├── templates/                # HTML templates
│   └── quotes/
│       └── index.html
│
└── requirements.txt          # Python dependencies
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

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create directory

```bash
mkdir storefront
cd storefront
```
### 6. Install Django
```bash
pip install django
```

### 7. Create Django project
```bash
python -m django startproject storefront .
``` 

### 8. Create Django app
```bash
python manage.py startapp quotes
```

### 8. Run the migrations
```bash
python manage.py migrate
```

### 10. Run the development server

```bash
python manage.py runserver
```

### 11. Access the application

Open your web browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## How It Works

1. The app initializes a Django web server
2. When a user accesses the homepage, the app attempts to fetch a random quote from the Quotable API
3. If the API call is successful, the quote is displayed
4. If the API is unavailable, a fallback quote is randomly selected from the predefined list
5. Users can get a new quote by clicking the "New Quote" button, which uses AJAX to fetch a new quote without reloading the page

## API Reference

The application attempts to fetch quotes from the [Quotable API](https://api.quotable.io/random).

## Django Documentation

For more information about Django:
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- [Django REST Framework](https://www.django-rest-framework.org/) (if you want to expand the API)

 