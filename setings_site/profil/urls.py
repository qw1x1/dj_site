from django.urls import path
from .views import *

app_name = 'prof'

urlpatterns = [
    path('profil_settings/', SettingsProfil.as_view(), name='profil_settings'),
]