from django.shortcuts import render
from django.http import JsonResponse
from .services import get_random_quote

def index(request):
    """View for the homepage"""
    quote = get_random_quote()
    return render(request, 'quotes/index.html', {'quote': quote})

def get_quote(request):
    """API endpoint to get a new random quote"""
    quote = get_random_quote()
    return JsonResponse({
        'text': quote.text,
        'author': quote.author
    })