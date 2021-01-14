
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
        path('movieView/', views.movie_view.as_view()),

        path('', views.home, name="homepage"),
        path('signup/', views.signup, name="signup"),
        path('login/', views.login_view, name="login"),
        path('logout/', views.logout_view, name="logout"),
        path('home/', views.blank, name="homepage redirect"),
        path('profilePage/', views.profile_view, name="profile"),
        path('movie/<slug:movie_id>/', views.specific_movie, name="moviePage"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
