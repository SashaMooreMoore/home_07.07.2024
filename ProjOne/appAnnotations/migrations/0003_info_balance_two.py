# Generated by Django 5.0.6 on 2024-06-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAnnotations', '0002_alter_info_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='balance_two',
            field=models.FloatField(default=340.5, verbose_name='Второй баланс'),
        ),
    ]
