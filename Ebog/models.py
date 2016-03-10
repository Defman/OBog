from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=32)

    content = RichTextField()

    description = models.TextField()

    tags = TaggableManager()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Section(models.Model):
    title = models.CharField(max_length=32)
    pages = SortedManyToManyField(Page)

    description = models.TextField()

    tags = TaggableManager()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=32)
    sections = SortedManyToManyField(Section)

    thumbnail = ImageField(upload_to="books/thumbnails")

    description = models.TextField()

    tags = TaggableManager()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        reverse("ebook:detail", self.slug);