# Generated by Django 2.2.27 on 2022-04-09 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add _slug_to_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='first_name',
            new_name='given_name',
        ),
    ]
