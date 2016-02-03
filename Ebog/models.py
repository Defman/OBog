from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField

# Create your models here.


class tag(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class page(models.Model):
    title = models.CharField(max_length=32)

    content = RichTextField()

    description = models.TextField()

    tags = models.ManyToManyField(tag)

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class section(models.Model):
    title = models.CharField(max_length=32)
    pages = SortedManyToManyField(page)

    description = models.TextField()

    tags = models.ManyToManyField(tag)

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class book(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=32)
    sections = SortedManyToManyField(section)

    tags = models.ManyToManyField(tag)

    description = models.TextField()

    author = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)