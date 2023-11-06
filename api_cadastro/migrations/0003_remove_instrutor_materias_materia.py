# Generated by Django 4.2.3 on 2023-10-17 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api_cadastro", "0002_sala_rename_cad_instrutor_instrutor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instrutor",
            name="materias",
        ),
        migrations.CreateModel(
            name="Materia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=60)),
                (
                    "instrutor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cadastro.instrutor",
                    ),
                ),
            ],
        ),
    ]