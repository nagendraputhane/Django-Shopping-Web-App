# Generated by Django 2.1.1 on 2018-11-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('click_collect', '0002_todoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='content',
            field=models.CharField(max_length=64),
        ),
    ]
