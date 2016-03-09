from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.


class SlideFront(models.Model):
    image = ImageField(upload_to="slides/front")

    text = models.TextField(null=True)