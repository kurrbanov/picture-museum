from django.shortcuts import render, HttpResponse

from .models import Picture, Author


def main_page(request):
    return render(request, 'main.html')


def all_pictures_view(request):
    pictures = Picture.objects.all()
    return render(request, 'list.html', context={'pictures': pictures, 'authors': None})


def all_authors_view(request):
    authors = Author.objects.all()
    return render(request, 'list.html', context={'pictures': None, 'authors': authors})


def show_picture(request, pk):
    try:
        picture = Picture.objects.get(id=pk)
    except Picture.DoesNotExist:
        return HttpResponse(request, 'Картина не существует')

    return render(request, 'info_html.html', context={'picture': picture, 'author': None})


def show_author(request, pk):
    try:
        author = Author.objects.get(id=pk)
    except Author.DoesNotExist:
        return HttpResponse(request, 'Автор не существует')

    return render(request, 'info_html.html',
                  context={'picture': None, 'author': author, 'author_pics': author.picture_set.all()})
