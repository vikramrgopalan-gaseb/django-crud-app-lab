from django.contrib import admin
from .models import Sneaker, Collection, Condition

admin.site.register(Sneaker)
admin.site.register(Collection)
admin.site.register(Condition)