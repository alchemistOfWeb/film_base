from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Film, Genre
from .forms import ReviewForm


class FilmsView(ListView):
    """ films list """
    model = Film
    context_object_name = 'films'
    template_name = 'film_list'

    by = [
        'title',
        'actors__name',
        'directors__name',
    ]

    def filter_films(self):
        request_by = self.request.GET['by']
        params = {}

        if request_by:
            params[f'{self.by[int(request_by)]}__icontains'] \
                = self.request.GET.get('search')

        genre_list = self.request.GET.getlist("genre")

        if genre_list:
            params['genres__id__in'] = genre_list

        print(params)

        filtered = Film.objects.filter(**params).distinct()
        print(filtered)
        return filtered

    def get_queryset(self):
        if self.request.GET:
            return self.filter_films()

        return Film.objects.all()


class FilmDetailView(DetailView):
    """ show the film """
    model = Film
    pk_url_kwarg = 'film_pk'
    template_name = 'films/film_detail.html'


class AddReview(View):
    def post(self, request, film_pk):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.film_id = film_pk
            form.save()

        return redirect("/")


# class FilterFilmsView(ListView):
#     def get_queryset(self):
#         possibles = {'actor','film_title', 'director'}
#         search_by = {}
#
#         queryset = Film.objects.filter(
#             actor=self.request.GET.get
#             genre__in=self.request.GET.getlist("genre")
#         )


# class SearchFilm(ListView):
#     def get_queryset(self):
#         return Film.objects.filter

class EditFilm(View):
    ...



