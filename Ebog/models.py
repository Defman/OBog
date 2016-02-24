from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=32)
    agdescription = models.TextField()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Page(models.Model):
    title = models.CharField(max_length=32)

    content = RichTextField()

    description = models.TextField()

    tags = models.ManyToManyField(Tag)

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Section(models.Model):
    title = models.CharField(max_length=32)
    pages = SortedManyToManyField(Page)

    description = models.TextField()

    tags = models.ManyToManyField(Tag)

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=32)
    sections = SortedManyToManyField(Section)

    tags = models.ManyToManyField(Tag)

    description = models.TextField()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)