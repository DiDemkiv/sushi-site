# Generated by Django 4.0.3 on 2022-03-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='img',
            field=models.ImageField(upload_to='article'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]