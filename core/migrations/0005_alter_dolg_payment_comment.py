# Generated by Django 5.0.6 on 2024-06-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_dolg_payment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolg',
            name='payment_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий к оплате'),
        ),
    ]