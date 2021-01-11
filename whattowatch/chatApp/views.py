from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        "title":"Homepage",
        }
    return render(request, "base.html", context=context)
