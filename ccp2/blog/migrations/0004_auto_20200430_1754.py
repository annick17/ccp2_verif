# Generated by Django 3.0.5 on 2020-04-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200430_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
