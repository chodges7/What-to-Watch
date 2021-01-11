from django.contrib.auth import login, logout
from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from imdb import IMDb
from . import models
from . import forms

@login_required(login_url="/login/")
def blank(request):
    return redirect("/home/")

@login_required(login_url="/login/")
def home(request):
    # Get top movies
    movies_data = IMDb()
    top = movies_data.get_top250_movies()

    if request.method == "POST":
        form_search = forms.SearchForm(request.POST)
        if form_search.is_valid():
            search = movies_data.search_movie(form_search.cleaned_data["search_field"])
            top_movie_id = search[0].getID()
            new_url = "/movie/" + top_movie_id + "/"
            form_search = forms.SearchForm()
            return redirect(new_url)
    else:
        form_search = forms.SearchForm()

    context = {
        "form_search":form_search,
        "title":'WTW Home',
        "movies":top,
    }
    return render(request,'home.html', context=context)

@login_required(login_url="/login/")
def specific_movie(request, movie_id):
    #Grab movie in database from person argument
    movies_data = IMDb()
    movie = movies_data.get_movie(movie_id)
    #print(movie.keys())

    if request.method == "POST":
        form_search = forms.SearchForm(request.POST)
        if form_search.is_valid():
            search = movies_data.search_movie(form_search.cleaned_data["search_field"])
            print(search)
            print(search[0].keys())
            top_movie_id = search[0].getID()
            new_url = "/movie/" + top_movie_id + "/"
            form_search = forms.SearchForm()
            return redirect(new_url)
    else:
        form_search = forms.SearchForm()

    context = {
        "cover":movie['full-size cover url'],
        "form_search":form_search,
        "title":movie['title'],
        "movie":movie,
        }
    return render(request, "specific_movie.html", context=context)

@login_required(login_url="/login/")
def profile_view(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    welc = "Welcome to your profile page: "
    welc += prof.profile_fname + " " + prof.profile_lname

    # FORMS for this page
    if request.method == "POST":
        form = forms.BioForm(request.POST)
        if form.is_valid():
            prof.profile_bio = form.cleaned_data["profile_bio"]
            prof.save()
            form = forms.BioForm()
            return redirect('/profilePage/')
    else:
        form = forms.BioForm()
    if request.method == "POST" and not form.is_valid():
        form_picture = forms.PictureForm(request.POST, request.FILES)
        if form_picture.is_valid():
            prof.profile_image = form_picture.cleaned_data["profile_image"]
            prof.save()
            form_picture = forms.PictureForm()
            return redirect('/profilePage/')
    else:
        form_picture = forms.PictureForm()

    context = {
        "body":welc,
        "form":form,
        "form_picture":form_picture,
        "title":"WTW Profile",
        "bio":prof.profile_bio,
        "profile_picture":prof.profile_image,
    }
    return render(request, "profile_page.html", context=context)

def login_view(request):
    # Authentication works
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')
    else:
        form = AuthenticationForm()

    context = {
        "form":form,
        "title":"WTW Login",
    }
    return render(request,'login.html', context=context)

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/home/")

def signup(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
        "title":"WTW Register",
        }
    return render(request, "signup.html", context=context)
