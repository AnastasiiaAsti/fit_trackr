# Generated by Django 4.2.16 on 2024-09-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_workout_muscle_group_alter_workout_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
