from django.views import generic


class index(generic.TemplateView):
    template_name = "store_index.html"

    title = "Obog - store"
    description = ""