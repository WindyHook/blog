# Generated by Django 3.0.3 on 2020-03-01 14:37

import article.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(default=article.models.set_default_column, on_delete=django.db.models.deletion.SET_DEFAULT, to='article.ArticleColumn'),
        ),
    ]
