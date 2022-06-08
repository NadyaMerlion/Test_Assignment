import cmath
from django.shortcuts import render
from .models import Number
from .forms import NumberForm


def index(request):
    """Функция отображения для домашней страницы сайта."""
    template = 'index.html'
    return render(request, template)


# def result(request):
#     # a, b, c = Number.objects.all()
#     # discrement = (b**2) - (4 * a*c)
#     # result1 = (-b-cmath.sqrt(discrement))/(2 * a)
#     # result2 = (-b + cmath.sqrt(discrement))/(2 * a)
#     template = 'index.html'
#     form = NumberForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save(commit=True)
#             return result1, result2
#     form = NumberForm()
#     context = {
#         'result1': result1,
#         'result2': result2,
#         'form': form
#     }
#     return render(request, template, context)
