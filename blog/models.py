from datetime import datetime
from os import remove

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
  slug = models.SlugField(unique=True)
  author = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=50)
  content = models.TextField()
  summary = models.TextField()

  def save(self,*args, **kwargs):
    if self.slug is None or self.slug == "":
      self.slug = slugify(self.title)
      if self.__class__.objects.filter(slug = self.slug).exists():
        self.slug = self.slug+f"{str(datetime.now().strftime('%M:%S:%f')[:-2]).replace(':','-')}"
    super().save(*args, **kwargs)
