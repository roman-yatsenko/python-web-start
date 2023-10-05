from django.db import models

# Create your models here.

class BoardMessage(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Опис')
    price = models.FloatField(null=True, blank=True, verbose_name='Ціна')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано')

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'
        ordering = ['-published']
    