# Generated by Django 2.2.3 on 2019-08-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
