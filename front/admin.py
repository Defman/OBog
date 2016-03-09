from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(SlideFront)
class SliderAdmin(admin.ModelAdmin):
    pass