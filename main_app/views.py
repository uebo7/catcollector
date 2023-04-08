from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
# NOTE: class-based views are classes that create view function objects containing
# pre-defined controller logic commonly used for basic CRUD operations
# their main benefit is to provide convenience to developers
from .models import Cat, Toy
from .forms import FeedingForm

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
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat, 
        'feeding_form': feeding_form
    })


def add_feeding(request, cat_id):
    # create a new model instance of feeding
    form = FeedingForm(request.POST) # {'meal': 'B', date: '2023-04-05', cat_id: None}
    # validate user input provided from form submission
    if form.is_valid():
       new_feeding = form.save(commit=False) # create an in-memory instance without saving to the database
       new_feeding.cat_id = cat_id # attach the associated cat's id to the cat_id attr
       new_feeding.save() # this will save a new feeding to the database
    # as long as form is valid we can associate the related cat to the new feeding
    # return a redirect response to the client
    return redirect('cat_detail', cat_id=cat_id)

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

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    template_name = 'toys/toy_form.html'

class ToyList(ListView):
    model = Toy
    template_name = 'toys/toy_list.html'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/toy_detail.html'
    
class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'
    template_name = 'toys/toy_form.html'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
    template_name = 'toys/toy_confirm_delete.html'