# Generated by Django 4.2.1 on 2023-05-16 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_cadastrados_nasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrados',
            name='bairro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='cidade',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='enc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='end',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='estado',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='genero',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='mae',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='motivo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='naturalidade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='nis',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='pai',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='parentesco',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='resp',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='rg',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cadastrados',
            name='sus',
            field=models.CharField(max_length=20),
        ),
    ]
