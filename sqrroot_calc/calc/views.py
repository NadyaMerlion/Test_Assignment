from django.shortcuts import render
from .forms import NumberForm


def index(request):
    """Функция отображения для домашней страницы сайта."""
    template = 'index.html'
    return render(request, template)


def result(request):
    template = 'index.html'
    form = NumberForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
    form = NumberForm()
    context = {
        'form': form
    }
    return render(request, template, context)
