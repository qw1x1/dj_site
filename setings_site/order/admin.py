from django.contrib import admin
from .models import *

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_slug_list', 'total_price', 'number_phon', 'tranzit')
    list_display_links = ('id', 'user')
    search_fields = ('user',)

admin.site.register(Orders, OrdersAdmin)