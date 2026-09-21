from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

USER = get_user_model()
        
class Todo(models.Model):
    owner = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,  
        related_name='todos',      
        verbose_name='Владелец'
    )
    title = models.CharField('Наименование', max_length=255)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    completed_at = models.DateTimeField('Дата выполнения', null=True, blank=True)
    note = models.TextField('Примечание', blank=True)
    is_completed = models.BooleanField('Выполнено', default=False)

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'
        ordering = ['-created_at']  # Новые дела сверху
