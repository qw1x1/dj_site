from .models import *
from django.db.models import Count
from django.core.cache import cache
from django.db.models import Sum
import re


menu = [{'title': "О нас", 'url_name': 'home'},
        {'title': "Доставка", 'url_name': 'home'},
        {'title': "Способы оплаты", 'url_name': 'home'},
        {'title': "Корзина", 'url_name': 'cart'},
]

class DataMixin:
    paginate_by = 7

    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.all()

        try:
            self.request.session['total_price'] = float(Product.objects.filter(available=True, slug__in=self.request.session.get('cart')).aggregate(Sum('price'))['price__sum'])
        except:
            self.request.session['total_price'] = str('0,00')

        if self.request.user.is_authenticated:
            context['menu'] = menu[:3]    
        else:
            context['menu'] = menu
            
        context['category'] = category
 
        return context

    @staticmethod
    def validate_nuber_phone(nuber_phone):
        return re.findall(r'(\+375|80|375).*?(\d{2}.*?\d{3}.*?\d{2}.*?\d{2})', nuber_phone)

    @staticmethod
    def validate_birth_date(birth_date):
        return re.findall(r'(\d{4}-\d\d-\d\d)', birth_date)

    @staticmethod
    def validate_mail(mail):
        return re.findall(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', mail)