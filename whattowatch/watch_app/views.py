from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from imdb import IMDb
from . import serializers
from . import forms
from . import models


class MovieView(generics.ListAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

class AddMovieView(APIView):
    serializer_class = serializers.AddMovieSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            rotten_tomatos = serializer.data.get('rotten_tomatos') # TESTING
            # If I had an api to find the urls for amazon, netflix, etc
            # I would put them here as:
            # amazon_url = APII'mUsing(movieTitle)

            # This if statement checks to see if a movie with that title already
            # exists in the database and just updates the fields of it
            queryset = models.Movie.objects.filter(title=title)
            if queryset.exists():
                movie = queryset[0]
                movie.title = title
                movie.set_movie_id()
                movie.rotten_tomatos = rotten_tomatos # TESTING
                # existingMovie.amazon_url = APII'mUsing(movieTitle) ...
                movie.save(update_fields=['title',])
            else:
                movie = models.Movie(title=title, rotten_tomatos=rotten_tomatos)
                movie.set_movie_id()
                movie.save()

            return Response(serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
        return Response(serializers.MovieSerializer(), status=status.HTTP_400_BAD_REQUEST)



def blank(request):
    # this redirects to the homepage to not deal with the hastle of using
    # weird href links
    return redirect("homepage")

def home(request):
    # Get top movies
    movies_data = IMDb()
    top = movies_data.get_top250_movies()

    if request.method == "POST":
        form_search = forms.SearchForm(request.POST)
        if form_search.is_valid():
            search = movies_data.search_movie(form_search.cleaned_data["search_field"])
            top_movie_id = search[0].getID()
            new_url = "/api/movie/" + top_movie_id + "/"
            form_search = forms.SearchForm()
            return redirect(new_url)
    else:
        form_search = forms.SearchForm()

    context = {
        "form_search":form_search,
        "title":'WTW Home',
        "movies":top,
    }
    return render(request,'watch_app/home.html', context=context)

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
            new_url = "/api/movie/" + top_movie_id + "/"
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
    return render(request, "watch_app/specific_movie.html", context=context)

@login_required(login_url="login")
def profile_view(request):
    prof = request.user
    welc = "Welcome to your profile page: "
    welc += prof.first_name + " " + prof.last_name

    # FORMS for this page
    if request.method == "POST":
        form_bio = forms.BioForm(request.POST)
        if form_bio.is_valid():
            prof.bio = form_bio.cleaned_data["bio"]
            prof.save()
            form_bio = forms.BioForm()
            return redirect('/api/profilePage/')
    else:
        form_bio = forms.BioForm()
    if request.method == "POST" and not form_bio.is_valid():
        form_picture = forms.PictureForm(request.POST, request.FILES)
        if form_picture.is_valid():
            prof.profile_picture = form_picture.cleaned_data["profile_picture"]
            prof.save()
            form_picture = forms.PictureForm()
            return redirect('/api/profilePage/')
    else:
        form_picture = forms.PictureForm()

    context = {
        "body":welc,
        "form_bio":form_bio,
        "form_picture":form_picture,
        "title":"WTW Profile",
        "prof":prof,
    }
    return render(request, "watch_app/profile_page.html", context=context)

def login_view(request):
    # Authentication works
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("homepage")
    else:
        form = AuthenticationForm()

    context = {
        "form":form,
        "title":"WTW Login",
    }
    return render(request,'watch_app/login.html', context=context)

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("homepage")

def signup(request):
    if request.method == "POST":
        form_instance = forms.CustomUserCreationForm(request.POST, request.FILES)
        if form_instance.is_valid():
            new_user = form_instance.save()
            new_user = authenticate(username=form_instance.cleaned_data["email"],
                                    password=form_instance.cleaned_data["password1"])
            login(request, new_user)
            return redirect("homepage")
    else:
        form_instance = forms.CustomUserCreationForm()
    context = {
        "form":form_instance,
        "title":"WTW Register",
        }
    return render(request, "watch_app/signup.html", context=context)
