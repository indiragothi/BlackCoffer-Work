import requests
import random
import urllib3
from .models import Quote

# Disable SSL warnings - only for development
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List of fallback quotes
fallback_quotes = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "Your time is limited, don't waste it living someone else's life.", "author": "Steve Jobs"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"text": "Hard work beats talent when talent doesn't work hard.", "author": "Tim Notke"},
    {"text": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"text": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
    {"text": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "Everything you've ever wanted is on the other side of fear.", "author": "George Addair"},
    {"text": "Success is walking from failure to failure with no loss of enthusiasm.", "author": "Winston Churchill"},
    {"text": "The mind is everything. What you think you become.", "author": "Buddha"},
    {"text": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"}
]

def get_random_quote():
    """Fetch a random quote from an API or use fallback quotes"""
    try:
        response = requests.get('https://api.quotable.io/random', verify=False, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return Quote.from_dict(data)
        else:
            # Use fallback quotes if API fails
            quote_data = random.choice(fallback_quotes)
            return Quote(quote_data["text"], quote_data["author"])
    except Exception as e:
        # Use fallback quotes in case of any error
        print(f"Error fetching quote: {e}")
        quote_data = random.choice(fallback_quotes)
        return Quote(quote_data["text"], quote_data["author"])