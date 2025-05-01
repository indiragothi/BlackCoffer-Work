from django.db import models

class Quote:
    """
    A simple model class to represent a quote.
    Not a database model, just a data class.
    """
    def __init__(self, text, author):
        self.text = text
        self.author = author
    
    def __str__(self):
        return f"{self.text} - {self.author}"
    
    @staticmethod
    def from_dict(data):
        """Create a Quote object from dictionary data"""
        text = data.get('content', '')
        author = data.get('author', 'Unknown')
        return Quote(text, author)