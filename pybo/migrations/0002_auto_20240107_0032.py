# Generated by Django 3.2.10 on 2024-01-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateField(),
        ),
    ]