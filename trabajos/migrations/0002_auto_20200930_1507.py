# Generated by Django 2.2.3 on 2020-09-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='categoria',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Retapizado'), (2, 'Fabricacion'), (3, 'Unica')], default=1, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='descripcion',
            field=models.CharField(max_length=150, verbose_name='Descripción'),
        ),
    ]
