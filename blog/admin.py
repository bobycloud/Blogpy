from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Category)