# Generated by Django 2.2.1 on 2019-06-13 06:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm1', '0005_auto_20190607_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='namelink5',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
