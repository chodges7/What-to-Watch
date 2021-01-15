from django.shortcuts import render

# Create your views here.
def index(request): # , *args, **kwargs): commented out for linter errors
    return render(request, 'frontend/base.html')
