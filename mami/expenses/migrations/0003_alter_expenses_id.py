# Generated by Django 4.2.7 on 2023-11-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expenses_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]