# Generated by Django 4.2.1 on 2023-05-16 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrados',
            name='nasc',
            field=models.CharField(max_length=15),
        ),
    ]
