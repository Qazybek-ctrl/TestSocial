# Generated by Django 4.0.3 on 2022-04-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialperson',
            name='background',
            field=models.ImageField(default='', upload_to='backs'),
        ),
    ]
