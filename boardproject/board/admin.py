from django.contrib import admin
from .models import Thread, Response, Key

# Register your models here.
admin.site.register(Thread)
admin.site.register(Response)
admin.site.register(Key)