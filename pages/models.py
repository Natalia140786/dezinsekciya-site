from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Вопрос-ответ"
        verbose_name_plural = "Вопросы-ответы"
        ordering = ['order', 'question']

    def __str__(self):
        return self.question

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to='slider/', verbose_name="Изображение")
    title = models.CharField(max_length=200, blank=True, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Подзаголовок")
    link = models.URLField(blank=True, verbose_name="Ссылка (кнопка)")
    link_text = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки")
    order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядок")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ['order']

    def __str__(self):
        return self.title or f"Слайд {self.id}"