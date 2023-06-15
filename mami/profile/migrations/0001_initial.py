
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(db_index=True, max_length=255, verbose_name='Порода')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=50, verbose_name="ім'я улюбленця")),
                ('weight', models.FloatField(verbose_name='вага')),
                ('photo', models.ImageField(upload_to='static/pet_photo')),
                ('description', models.CharField(max_length=255, verbose_name='особливості')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeds', to='profile.breed')),
            ],
        ),
    ]