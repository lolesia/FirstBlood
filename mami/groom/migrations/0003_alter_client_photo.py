# Generated by Django 4.1.7 on 2023-02-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groom', '0002_alter_client_options_alter_expenses_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='static/groom', verbose_name='Фото'),
        ),
    ]
