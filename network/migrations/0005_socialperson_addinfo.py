# Generated by Django 4.0.3 on 2022-05-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_socialperson_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialperson',
            name='addInfo',
            field=models.CharField(max_length=150, null=True),
        ),
    ]