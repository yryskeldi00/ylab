# Generated by Django 4.0.1 on 2022-01-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('is_overdraft', models.BooleanField(default=False, verbose_name='Овердрафности')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Общая сумма денег на счете')),
            ],
            options={
                'verbose_name': 'Счет в банке',
                'verbose_name_plural': 'Счеты в банке',
            },
        ),
    ]