# Generated by Django 4.2.5 on 2023-10-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("autenticacion", "0003_alter_perfilusuario_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfilusuario",
            name="fecha_nacimiento",
            field=models.DateField(blank=True, null=True),
        ),
    ]
