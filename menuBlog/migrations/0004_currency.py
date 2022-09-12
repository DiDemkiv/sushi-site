# Generated by Django 4.0.3 on 2022-03-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuBlog', '0003_dish_gram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('symbol', models.CharField(max_length=3)),
            ],
        ),
    ]