# Generated by Django 3.0.3 on 2020-06-09 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clioncare', '0002_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='problem_since',
            field=models.CharField(max_length=10),
        ),
    ]
