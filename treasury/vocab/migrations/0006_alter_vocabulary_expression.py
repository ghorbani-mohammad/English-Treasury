# Generated by Django 4.1 on 2023-02-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0005_alter_profilevocabulary_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='expression',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
