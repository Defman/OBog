from django.contrib.messages import get_messages
from django.views import generic


class index(generic.TemplateView):
    template_name = "index.html"

    title = "Obog - the future is here"
    description = ""


class about(generic.TemplateView):
    template_name = "about.html"

    title = "Obog - the future is about"
    description = ""


class credits(generic.TemplateView):
    template_name = "credits.html"

    title = "Obog - the future is about"
    description = ""
