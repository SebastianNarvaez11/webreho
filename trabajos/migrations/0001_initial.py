# Generated by Django 2.2.3 on 2020-09-30 16:28

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import trabajos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Slug/Url')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido')),
                ('imagen1', models.ImageField(upload_to=trabajos.models.custom_upload_to1, verbose_name='Imagen 1')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to=trabajos.models.custom_upload_to2, verbose_name='Imagen 2')),
                ('index', models.BooleanField(default=True, verbose_name='Mostrar en el inicio')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/Oculto')),
                ('creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('edicion', models.DateField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Trabajos',
                'verbose_name_plural': 'Trabajos',
                'ordering': ['creacion'],
            },
        ),
    ]
