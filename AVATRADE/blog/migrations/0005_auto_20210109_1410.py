# Generated by Django 3.1.3 on 2021-01-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210109_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='full_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
