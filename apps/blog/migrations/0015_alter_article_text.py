# Generated by Django 4.0.6 on 2022-10-03 14:17

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_article_meta_description_article_meta_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='Текст'),
        ),
    ]
