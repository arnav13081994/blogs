# Generated by Django 2.2.3 on 2019-08-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190804_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='experience',
            field=models.IntegerField(choices=[(1, '< 1 year'), (2, '1-2 years'), (3, '2-5 years'), (4, '5+ years')], default='2'),
        ),
    ]