# Generated by Django 2.2 on 2021-09-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='hllo word', max_length=120),
            preserve_default=False,
        ),
    ]
