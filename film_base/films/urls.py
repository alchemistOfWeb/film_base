from django.urls import path

from .views import *


urlpatterns = [
    # path('', index),
    # path('<int:pk>/', show),
    # path('create_film/', create),
    # path('store_film/', store),
    # path('edit_film/<int:film_id>', edit),
    # path('update_film/<int:film_id>', update),
    # path('delete_film/<int:film_id>', delete),
    #
    # path('add_actor/'),
    # path('add_director/'),
    # path('add_genre/'),
    # path('add_genre/'),


    path('', FilmsView.as_view(), name='film_list'),
    path('<int:film_pk>', FilmDetailView.as_view(), name='film_detail'),

    path('<int:film_pk>', AddReview.as_view(), name='add_review'),

]
