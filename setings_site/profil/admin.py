from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'photo', 'number_phon', 'birth_date')
    list_display_links = ('id',)


admin.site.register(Profile, ProfileAdmin)
