from django.views import generic


class profile(generic.TemplateView):
    template_name = "profile.html"

    title = "Obog - min side - "
    description = ""


class mybooks(generic.ListView):
    template_name = "user_books.html"

    title = "Obog - mine bøger "
    description = ""

