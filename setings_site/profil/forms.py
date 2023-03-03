from django import forms
from .models import *

# class ProfilForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['photo']
#         fields = ['number_phon']
        
#     def clean_number_phon(self): # Валидатор доя поля title
#         print(self.cleaned_data['number_phon'])
#         number = self.cleaned_data['number_phon'] # Получаем данные из колекции cleaned_data (берём title)
#         if len(number) < 12:
#             raise ValidationError('Длина превышает 12 цифр')
#         if not number.isdigit():
#             raise ValidationError('Номер телефона должен состоять только из цифр')
#         return number

