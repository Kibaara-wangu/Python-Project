# Generated by Django 5.0.7 on 2024-07-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_id',
            field=models.IntegerField(),
        ),
    ]