from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, \
    DeleteView

from portal.models import Movie


class HomeView(ListView):
    template_name = 'movie_list.html'
    model = Movie
    queryset = Movie.objects.all()
    context_object_name = 'movie_list'


class MovieAddView(CreateView):
    template_name = 'movie_add.html'
    success_url = reverse_lazy('home')
    model = Movie
    fields = ['name', 'genre', 'studio', 'director', 'cast', 'collection', 'release_date']


class MovieUpdateView(UpdateView):
    template_name = 'movie_add.html'
    success_url = reverse_lazy('home')
    model = Movie
    fields = ['name', 'genre', 'studio', 'director', 'cast', 'collection', 'release_date']


class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('home')
    model = Movie
    fields = ['name', 'genre', 'studio', 'director', 'cast', 'collection', 'release_date']
