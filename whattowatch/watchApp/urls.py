
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
        path('', views.blank, name='blank'),
        path('home/', views.home, name="homepage"),
        path('login/', views.login_view, name="login"),
        path('signup/', views.signup, name="signup"),
        path('logout/', views.logout_view, name="logout"),
        path('profilePage/', views.profile_view, name="profile"),
        path('Letschat/', views.lets_chat, name='Letschat'),
        path('chat/<str:room_name>/', views.room, name='room'),
        path('movie/<slug:movie_id>/', views.specific_movie, name="moviePage"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
