from django.shortcuts import render, redirect
from django.views import View
from order.models import * 
from shop.models import Product
from profil.models import Profile
from django.contrib.auth.models import User
from django.db.models import F

# class ShopCart(View):

#     def post(self, slug ,**kwargs):
        
#         ss = kwargs
#         if not self.request.session.get('cart'):
#             self.request.session['cart'] = list()
#         else:
#             self.request.session['cart'] = list(self.request.session['cart'])

#         if slug not in self.request.session['cart']:
#             self.request.session['cart'].append(slug)
#             self.request.session.modified = True
            
#         return redirect(self.request.POST.get('url_form'))


def add(request, slug):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])

        if slug not in request.session['cart']:
            request.session['cart'].append(slug)
            request.session.modified = True
    print(request.session['cart'])
    return redirect(request.POST.get('url_form'))

def remove(request, slug):
    if request.method == 'POST':
        if slug in request.session['cart']:
            request.session['cart'].remove(slug)

        request.session.modified = True
    return redirect(request.POST.get('url_form'))

def order(request):
    if request.method == 'POST':
        # if request.user.is_authenticated:
        #     profil = Profile.objects.filter(user__pk= int(request.POST.get('users')))
        #     profil_number_phon = profil.number_phon
        #     if len(profil_number_phon) > 7:
        #         print(profil_number_phon)

        Orders.objects.create( user= int(request.POST.get('users')), 
                        product_slug_list= request.session['cart'], total_price= request.session['total_price'], 
                        number_phon= int(request.POST.get('number')), tranzit= request.POST.get('tranzit')) 
        
        Product.objects.filter(slug__in=request.session.get('cart')).update(colum=F('colum') - 1)
 
        del request.session['cart']
        request.session.modified = True
    return redirect(request.POST.get('url_form'))