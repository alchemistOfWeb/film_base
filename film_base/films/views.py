from django.contrib import messages
from django.http import request
from django.http.response import JsonResponse
from .forms import RatingForm
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Actor, Director, Film, Genre, Review, Score
# from .forms import ReviewForm


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


        filtered = Film.objects.filter(**params).distinct()

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


class FilmEditView(LoginRequiredMixin, View):
    permission_denied_message = "NO! You are not authenticated for this action!"
    login_url = 'login/'
    raise_exception = True

    def get(self, request, film_pk):

        filtered_actors = Actor.objects.exclude(films__id=film_pk)
        filtered_directors = Director.objects.exclude(films__id=film_pk)

        context = {'film': Film.objects.get(pk=film_pk), 'actors': filtered_actors, 'directors': filtered_directors}

        return render(request, template_name='films/edit.html', context=context)

    def post(self, request, film_pk):
        print(request.POST)
        
        film = Film.objects.get(pk=film_pk)
        film.actors.set(request.POST.getlist('actors'))
        film.directors.set(request.POST.getlist('directors'))

        messages.success(request, 'success')
        return redirect(reverse('edit_film', args=[film_pk]))


class AddRatingStar(LoginRequiredMixin, View):
    permission_denied_message = "NO! You are not authenticated for this action!"
    raise_exception = True
    
    def post(self, request, film_pk):

        # if not request.user.is_authenticated:
        # return JsonResponse({'status': 403, 'message': request.user.username})
            

        form = RatingForm(request.POST)

        if form.is_valid():
            Score.objects.update_or_create(
                author_id=request.user.pk,
                film_id=film_pk,
                defaults={
                    'value': request.POST.get('rating')
                }
            )
            film = Film.objects.get(pk=film_pk)
            
            return JsonResponse({'status': 201, 'average_score': '{0:1.1f}'.format(film.get_average_score()), 'user': request.user.id})
        else:
            return JsonResponse({'status': 400})


class AddReview(LoginRequiredMixin, View):
    permission_denied_message = "NO! You are not authenticated for this action!"
    raise_exception = True

    def post(self, request, film_pk):
        # print(request.POST.get('text'))
        Review.objects.create(
            film_id=film_pk,
            user_id=request.user.id,
            text=request.POST.get('text')
        )

        return redirect(reverse('film_detail', args=[film_pk]))


# class AddReview(View):
#     ...
    # def post(self, request, film_pk):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.film_id = film_pk
    #         form.save()

    #     return redirect(reverse('film', ))

