from django.shortcuts import render

# Create your views here.
def base(request):
    context = {
        "title":"Chat Homepage",
        }
    return render(request, "base.html", context=context)
