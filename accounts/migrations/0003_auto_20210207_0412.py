# Generated by Django 3.1.6 on 2021-02-07 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_poem_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='auth',
            new_name='author',
        ),
    ]
