from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  sulg = models.SlugField(unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=50)
  content = models.TextField()
  summary = models.TextField()
