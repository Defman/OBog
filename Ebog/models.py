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
    pages = models.ManyToManyRel(page)

    description = models.TextField

    tags = models.ManyToManyRel(tag)

    author = models.ManyToOneRel(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class page(models.Model):
    content = RichTextField()

    description = models.TextField

    tags = models.ManyToManyRel(tag)

    author = models.ManyToOneRel(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class book(models.Model):
    slug = models.SlugField
    title = models.CharField
    sections = models.ManyToManyRel(section)

    tags = models.ManyToManyRel(tag)

    description = models.TextField

    author = models.ManyToOneRel(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)