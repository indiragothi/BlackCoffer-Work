from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(max_length=100, label='Title')
    description = forms.CharField(widget=forms.Textarea, required=False, label='Description')
    completed = forms.BooleanField(required=False, label='Completed')