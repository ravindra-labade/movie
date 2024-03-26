from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required


def add_movie(request):
    template_name = 'movie/add.html'
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_movie(request):
    template_name = 'movie/show.html'
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, template_name, context)


def update_movie(request, pk):
    template_name = 'movie/add.html'
    obj = Movie.objects.get(id=pk)
    form = MovieForm(instance=obj)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_movie(request, pk):
    obj = Movie.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'movie/confirm.html')
