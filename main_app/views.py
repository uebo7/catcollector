from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# NOTE: class-based views are classes that create view function objects containing
# pre-defined controller logic commonly used for basic CRUD operations
# their main benefit is to provide convenience to developers
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


class CatCreate(CreateView):
    model = Cat
    fields = '__all__' # adds all the fields to the corresponding ModelForm
    template_name = 'cats/cat_form.html'
    # success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields = ('description', 'age') # tuples are preferred over lists for the field attr
    template_name = 'cats/cat_form.html'
    # tuples are lightweight and use less space (memory)

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
    template_name = 'cats/cat_confirm_delete.html'