from django.db import models
from django.utils import timezone

class Order(models.Model):
    

    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    message = models.TextField(blank=True, verbose_name="Сообщение")
    service = models.CharField(max_length=100, blank=True, verbose_name="Услуга")
    area = models.CharField(max_length=50, blank=True, verbose_name="Площадь помещения")
    preferred_time = models.CharField(max_length=100, blank=True, verbose_name="Удобное время")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата заявки")
    is_processed = models.BooleanField(default=False, verbose_name="Обработано")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.created_at.strftime('%d.%m.%Y %H:%M')})"
