# Generated by Django 3.0.5 on 2020-05-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200502_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='accroche',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
