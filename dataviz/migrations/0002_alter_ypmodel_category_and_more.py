# Generated by Django 4.0.5 on 2022-06-14 02:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataviz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ypmodel',
            name='category',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ypmodel',
            name='sentence_entities',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=2), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ypmodel',
            name='sentence_keywords',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=2), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ypmodel',
            name='sentence_non_entities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='ypmodel',
            name='sentence_sentiment_label',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ypmodel',
            name='sentence_short',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
    ]
