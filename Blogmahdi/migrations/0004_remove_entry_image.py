# Generated by Django 2.1.7 on 2019-06-09 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogmahdi', '0003_auto_20190608_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='image',
        ),
    ]