# Create your models here.
from django.db import models

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя {attr verbose_name}')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон {attr verbose_name}')

    def __str__(self):
        return f'{self.id} {self.order_name}'

    class Meta:
        verbose_name = 'Заказ (Это сделал class Meta)'
        verbose_name_plural = 'Заказы (Это сделал class Meta)'

