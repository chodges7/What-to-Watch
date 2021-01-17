from django.shortcuts import render

# Create your views here.
def index(request): # , *args, **kwargs): commented out for linter errors
    context = {
        "title":"front_end views title",
    }
    return render(request, 'frontend/base.html', context=context)
