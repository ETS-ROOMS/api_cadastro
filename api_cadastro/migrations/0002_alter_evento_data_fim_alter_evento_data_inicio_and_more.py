# Generated by Django 4.2.3 on 2023-08-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data_fim',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_fim',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
