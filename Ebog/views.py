from django.views import generic
from .forms import *
from .models import *
from django.core.urlresolvers import reverse_lazy


# Create your views here.


class Book:
    class List(generic.ListView):
        template_name = "book_list.html"
        model = Book
        paginate_by = 10
        page_kwarg = "page"

    class Detail(generic.DetailView):
        model = Book
        template_name = "book_view.html"

    class Create(generic.CreateView):
        model = Book
        template_name = "form.html"
        form_class = BookFormCreate
        success_url = reverse_lazy('ebook:list')



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
