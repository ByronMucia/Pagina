# Generated by Django 4.2.5 on 2023-10-17 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("autenticacion", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="perfilusuario",
            old_name="user",
            new_name="username",
        ),
    ]
