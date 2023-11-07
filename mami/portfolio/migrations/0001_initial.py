# Generated by Django 4.2.7 on 2023-11-07 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='static/portfolio')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='portfolio', to='pets.breed')),
                ('groomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='profiles.groomer')),
            ],
        ),
    ]
