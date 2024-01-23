# Generated by Django 5.0.1 on 2024-01-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='home')),
            ],
        ),
    ]