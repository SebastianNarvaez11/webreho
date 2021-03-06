# Generated by Django 2.2.3 on 2020-10-02 17:06

import blog.models
import ckeditor_uploader.fields
import core.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20, unique=True, validators=[core.validators.validate_only_letters, django.core.validators.MinLengthValidator(3)], verbose_name='Titulo')),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido')),
                ('imagen', models.ImageField(upload_to=blog.models.custom_upload_to, verbose_name='Imagen')),
                ('slug', models.SlugField(verbose_name='Slug/Url')),
                ('publicacion', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion')),
                ('creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('edicion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('hora', models.DateTimeField(auto_now_add=True, verbose_name='Hora creacion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-hora'],
            },
        ),
    ]
