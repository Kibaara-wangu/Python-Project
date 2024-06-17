# Generated by Django 3.2.12 on 2024-06-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('number_of_seats', models.IntegerField()),
                ('number_of_students', models.IntegerField()),
                ('class_teacher', models.CharField(max_length=20)),
                ('courses', models.CharField(max_length=25)),
                ('available_equipments', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
