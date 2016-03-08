from django.views import generic
from .forms import *
from .models import *


# Create your views here.


class Book:
    class Detail(generic.DetailView):
        model = Book
        template_name = "Ebog/detail.html"

    class Create(generic.CreateView):
        model = Book
        template_name = "form.html"
        form_class = BookFormCreate



    class Edit(generic.UpdateView):
        model = Book
        form_class = BookFormCreate

    class Delete(generic.DeleteView):
        model = Book


class Section:
    class Detail(generic.DetailView):
        model = Book
        template_name = "Ebog/detail.html"

    class Create(generic.CreateView):
        model = Book
        form_class = BookFormCreate

    class Edit(generic.UpdateView):
        model = Book
        form_class = BookFormCreate

    class Delete(generic.DeleteView):
        model = Book


class Page:
    class Detail(generic.DetailView):
        model = Book
        template_name = "Ebog/detail.html"

    class Create(generic.CreateView):
        model = Page
        template_name = "form.html"
        form_class = PageForm

    class Edit(generic.UpdateView):
        model = Book
        form_class = BookFormCreate

    class Delete(generic.DeleteView):
        model = Book
