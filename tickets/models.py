
from django.db import models


class Ticket(models.Model):

    PRIORITY_CHOICES = [
        ('Low', 'Төмен'),
        ('Medium', 'Орташа'),
        ('High', 'Жоғары'),
    ]

    STATUS_CHOICES = [
        ('New', 'Жаңа'),
        ('In Progress', 'Орындалуда'),
        ('Completed', 'Аяқталды'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name='Тақырып'
    )

    description = models.TextField(
        verbose_name='Сипаттама'
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium',
        verbose_name='Басымдық'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New',
        verbose_name='Мәртебе'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
