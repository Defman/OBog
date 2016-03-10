from django.contrib.messages import get_messages
from django.views import generic
from django.contrib.staticfiles.templatetags.staticfiles import static
from .forms import *
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy


class index(generic.TemplateView):
    template_name = "index.html"

    title = "Obog - The New Future"
    description = ""

    images = []

    images.append(static("img/101_how_to_cpomute.png"))
    images.append(static("img/404_how_to_copmute.png"))


class about(generic.TemplateView):
    template_name = "about.html"

    title = "Obog - the future is about"
    description = ""


class credits(generic.TemplateView):
    template_name = "credits.html"

    title = "Obog - the future is about"
    description = ""


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "form.html"
    success_url = reverse_lazy("front:thankyou")
    

class ThankYou(generic.TemplateView):
    template_name = "thankyou.html"