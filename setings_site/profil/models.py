from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from datetime import datetime

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.PROTECT, null= True, db_index = True, verbose_name= 'Пользователь')
    photo = models.ImageField(upload_to="user_photos/", verbose_name= 'Фото', null=True)
    birth_date = models.DateField(auto_now=False, null=True, blank=True, verbose_name= 'День рожденья')
    number_phon = models.CharField(max_length=12, null= True, verbose_name= 'Номер телефона')

    def __str__(self):
        return str(self.user)

    def age(self):
        current_datetime = datetime.now() 
        return current_datetime.year - self.birth_date.year
            
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()