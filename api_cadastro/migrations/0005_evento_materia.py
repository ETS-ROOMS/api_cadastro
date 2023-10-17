# Generated by Django 4.2.3 on 2023-10-17 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api_cadastro", "0004_rename_id_evento_evento_id_evento_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="evento",
            name="materia",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="api_cadastro.materia",
            ),
            preserve_default=False,
        ),
    ]
