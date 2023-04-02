from django.shortcuts import render
from .models import Cat

# we use this file to define controller logic
# NOTE: each controller is defined using either a function or a class
# NOTE responses are returned from view functions
# NOTE: all views function take at least one required positional argument: request

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

# NOTE: url params are explicitly passed to view functions seperate from the request object
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})
