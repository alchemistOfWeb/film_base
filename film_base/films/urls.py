from django.urls import path
from .views import *


urlpatterns = [
    path('', FilmsView.as_view(), name='film_list'),
    path('<int:film_pk>', FilmDetailView.as_view(), name='film_detail'),
    path('<int:film_pk>/edit_film', FilmEditView.as_view(), name='edit_film'),
    path('<int:film_pk>/set_film_rating', AddRatingStar.as_view(), name='set_film_rating'),
    path('<int:film_pk>/add_review', AddReview.as_view(), name='add_review'),
    path('create_actor/', CreateActorView.as_view(), name='create_actor'),
    path('create_director/', CreateDirectorView.as_view(), name='create_director'),
]
