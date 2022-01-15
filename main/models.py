from django.db import models


class BankAccount(models.Model):
    """Bank Account"""
    title = models.CharField(verbose_name='Название', max_length=255)
    is_overdraft = models.BooleanField(
        verbose_name='Овердрафности', default=False
    )
    money = models.DecimalField(
        verbose_name='Общая сумма денег на счете', max_digits=12, decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Счеты в банке'
        verbose_name = 'Счет в банке'
