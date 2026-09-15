from django.db import models
from django.urls import reverse

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    slug = models.SlugField(unique=True, verbose_name="ЧПУ (для URL)")
    icon = models.ImageField(upload_to='services/icons/', blank=True, verbose_name="Иконка")
    short_description = models.TextField(max_length=300, verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Полное описание")
    seo_title = models.CharField(max_length=120, blank=True, verbose_name="SEO заголовок (title)")
    seo_description = models.CharField(max_length=250, blank=True, verbose_name="SEO описание (description)")
    price_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена от (руб)")
    methods = models.TextField(blank=True, verbose_name="Методы обработки")
    guarantee = models.CharField(max_length=100, default="6 месяцев", verbose_name="Гарантия")
    photo_before = models.ImageField(upload_to='services/before_after/', blank=True, verbose_name="Фото «до»")
    photo_after = models.ImageField(upload_to='services/before_after/', blank=True, verbose_name="Фото «после»")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядок")


    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:service_detail', args=[self.slug])