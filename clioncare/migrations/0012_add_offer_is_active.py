# Generated by Django 3.0.3 on 2020-06-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clioncare', '0011_add_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_offer',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]