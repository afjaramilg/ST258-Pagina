# Generated by Django 3.2 on 2021-05-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_alter_competitions_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitions',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
