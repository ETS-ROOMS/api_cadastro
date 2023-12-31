# Generated by Django 4.2.3 on 2023-10-17 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api_cadastro", "0003_remove_instrutor_materias_materia"),
    ]

    operations = [
        migrations.RenameField(
            model_name="evento",
            old_name="id_Evento",
            new_name="id_evento",
        ),
        migrations.RemoveField(
            model_name="evento",
            name="edv_cliente",
        ),
        migrations.RemoveField(
            model_name="evento",
            name="nome_responsavel",
        ),
        migrations.AddField(
            model_name="evento",
            name="instrutor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="api_cadastro.instrutor",
            ),
            preserve_default=False,
        ),
    ]
