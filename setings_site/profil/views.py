from shop.utils import DataMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Profile

class SettingsProfil(DataMixin, View):

    def get_context_data(self, **kwargs):
        context = self.get_user_context(title='Редактирование данных') # Плюс передаем в kwargs(в наш контекст) -> title
        return context

    def get(self, request):
        queryset = Profile.objects.get(user_id=request.user.pk)
        context = self.get_context_data()   
        context["profil"] = queryset
        return render(request, "profil/profile_settings.htm", context=context)

    def post(self, request):
        profil_pk = request.user.pk

        if request.POST.get('number_phon') or request.POST.get('photo') or request.POST.get('birth_date'):
            user_prof = Profile.objects.get(user_id=profil_pk)

            if request.POST.get('number_phon'):
                user_prof.number_phon = str(request.POST.get('number_phon'))

            if request.POST.get('photo'):
                user_prof.photo = "user_photos/" + str(request.POST.get('photo'))

            if request.POST.get('birth_date'):
                user_prof.birth_date = "-".join(request.POST.get('birth_date').split(".")[::-1])

            user_prof.save()

        if request.POST.get('mail') or request.POST.get('user_name'):
            user = User.objects.get(pk=profil_pk)

            if request.POST.get('mail'):
                user.email = str(request.POST.get('mail'))

            if request.POST.get('user_name'):
                user.first_name = str(request.POST.get('user_name'))

            user.save()
        return redirect('prof:profil_settings')