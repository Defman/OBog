from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    list_display = ('title', 'author')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
