from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class tag(models.Model):
    title = models.CharField
    description = models.TextField

    author = models.ManyToOneRel(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class section(models.Model):
    title = models.CharField
    pages = models.ManyToManyField(page)

    description = models.TextField

    tags = models.ManyToManyField(tag)

    author = models.ManyToOneFeild(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class page(models.Model):
    content = RichTextField()

    description = models.TextField

    tags = models.ManyToManyField(tag)

    author = models.ManyToOneField(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class book(models.Model):
    slug = models.SlugField
    title = models.CharField
    sections = models.ManyToManyField(section)

    tags = models.ManyToManyField(tag)

    description = models.TextField

    author = models.ManyToOneField(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)