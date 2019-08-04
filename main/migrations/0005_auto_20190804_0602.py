# Generated by Django 2.2.3 on 2019-08-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_author_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='experience',
            field=models.IntegerField(blank=True, choices=[('1', '< 1 year'), ('2', '1-2 years'), ('3', '2-5 years'), ('4', '5+ years')], null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
