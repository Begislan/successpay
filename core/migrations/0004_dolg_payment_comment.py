# Generated by Django 5.0.6 on 2024-06-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_dolg_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='dolg',
            name='payment_comment',
            field=models.TextField(blank=True, default='!', verbose_name='Комментарий к оплате'),
        ),
    ]