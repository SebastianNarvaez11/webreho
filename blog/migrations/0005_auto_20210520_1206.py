# Generated by Django 2.2.3 on 2021-05-20 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210518_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Titulo'),
        ),
    ]
