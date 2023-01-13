# Generated by Django 4.1.5 on 2023-01-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('user_req', models.TextField(max_length=1000)),
                ('description_ru', models.TextField(blank=True, max_length=1000)),
                ('error', models.TextField(blank=True, max_length=255)),
            ],
        ),
    ]
