# Generated by Django 4.0.3 on 2022-05-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialperson',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='socialperson',
            name='background',
            field=models.ImageField(blank=True, upload_to='backs'),
        ),
    ]