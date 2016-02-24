from django.views import generic
from .forms import *
from .models import *

# Create your views here.

class Book:
    class detail(generic.DetailView):
        model = Book
        template_name = "Ebog/detail.html"

    class create(generic.CreateView):
        model = Book
        template_name = "form.html"
        form_class = BookFormCreate

    class edit(generic.UpdateView):
        model = Book
        form_class = BookFormCreate

    class delete(generic.DeleteView):
        model = Book

    class Section:
        class detail(generic.DetailView):
            model = Book
            template_name = "Ebog/detail.html"

        class create(generic.CreateView):
            model = Book
            form_class = BookFormCreate

        class edit(generic.UpdateView):
            model = Book
            form_class = BookFormCreate

        class delete(generic.DeleteView):
            model = Book

        class Page:
            class detail(generic.DetailView):
                model = Book
                template_name = "Ebog/detail.html"

            class create(generic.CreateView):
                model = Book
                form_class = BookFormCreate

            class edit(generic.UpdateView):
                model = Book
                form_class = BookFormCreate

            class delete(generic.DeleteView):
                model = Book