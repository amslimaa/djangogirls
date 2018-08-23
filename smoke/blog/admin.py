from django.contrib import admin
from blog import models
from .models import Post

admin.site.register(Post)