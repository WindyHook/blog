# Generated by Django 3.0.4 on 2020-03-23 17:05

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
