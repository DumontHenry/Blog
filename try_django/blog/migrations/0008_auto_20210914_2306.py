# Generated by Django 2.2 on 2021-09-14 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210914_2301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
