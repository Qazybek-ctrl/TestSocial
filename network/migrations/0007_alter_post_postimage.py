# Generated by Django 4.0.3 on 2022-05-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(blank=True, null=True, upload_to='postImages'),
        ),
    ]
