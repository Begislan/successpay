# Generated by Django 5.0.6 on 2024-05-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_magazine_date_create_magazine'),
    ]

    operations = [
        migrations.AddField(
            model_name='dolg',
            name='phone_number',
            field=models.CharField(default='0', max_length=255, verbose_name='Номер телефона'),
        ),
    ]