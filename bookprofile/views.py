from django.views import generic


class Login(generic.TemplateView):
    pass


class Profile(generic.TemplateView):
    template_name = "profile.html"

    title = "Obog - min side - "
    description = ""


class Mybooks(generic.ListView):
    template_name = "user_books.html"

    title = "Obog - mine bøger "
    description = ""

