# Generated by Django 4.1 on 2023-02-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='long_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='short_description',
            field=models.TextField(null=True),
        ),
    ]