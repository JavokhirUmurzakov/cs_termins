# Generated by Django 4.0 on 2024-10-08 10:43

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_article_author_remove_article_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_body',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now, verbose_name='Maqola asosiy qismi'),
            preserve_default=False,
        ),
    ]
