# Generated by Django 3.0.3 on 2020-06-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clioncare', '0012_add_offer_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_offer',
            name='is_left_content',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='add_offer',
            name='is_left_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='add_offer',
            name='is_right_content',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='add_offer',
            name='is_right_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='add_offer',
            name='left_content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
