from django.db import models

from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

USER = get_user_model()
class Account(models.Model):
    owner = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        related_name='accounts',
        verbose_name='Владелец'
    )
    site = models.CharField('Сайт', max_length=255)
    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    created_at = models.DateTimeField('Дата создания',auto_now_add=True)
    password_changed_at = models.DateTimeField('Дата изменения пароля', auto_now=True)

    class Meta:
        verbose_name = 'Учетная запись'
        verbose_name_plural = 'Учетные записи'
        ordering = ['-created_at']

    def __str__(self):
            return f'{self.site} ({self.login})'
        
    def save(self, *args, **kwargs):
        if self.pk:
            old = Account.objects.filter(pk=self.pk).only('password').first()
            if old is not None and old.password != self.password:
                    self.password_changed_at = timezone.now()
            else:
                if not self.password_changed_at:
                    self.password_changed_at = timezone.now()

            super().save(*args, **kwargs)
            
