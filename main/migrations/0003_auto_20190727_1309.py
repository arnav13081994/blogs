# Generated by Django 2.2.3 on 2019-07-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default='static/main/images/article_generic.jpeg', upload_to=''),
        ),
    ]
