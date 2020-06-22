# Generated by Django 3.0.3 on 2020-06-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clioncare', '0010_auto_20200613_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(max_length=30)),
                ('background_image', models.ImageField(default='', upload_to='media/images')),
                ('offer_age', models.IntegerField()),
                ('font_family', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=150)),
                ('right_header', models.CharField(max_length=100)),
                ('left_header', models.CharField(max_length=100)),
                ('right_content', models.TextField()),
                ('offer_button_color', models.CharField(max_length=10)),
                ('offer_button_innertext', models.CharField(max_length=30)),
            ],
        ),
    ]