from django.db import models
from django.urls import reverse

# Create your models here.
class Orders(models.Model):
    user = models.IntegerField(null= True, db_index = True, verbose_name= 'Покупатель')
    product_slug_list = models.CharField(max_length=900, verbose_name= 'Покупки')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= 'Общая стоимость') 
    number_phon = models.CharField(max_length=12, verbose_name= 'Номер телефона')
    tranzit = models.CharField(max_length=30, null= True, verbose_name= 'Способ доставки')

    class Meta:
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупки'