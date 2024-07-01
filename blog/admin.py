from django.contrib import admin
from .models.Posts import Posts

models_list: list = [
    Posts
    ]



admin.site.register(models_list);