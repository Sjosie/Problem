# Generated by Django 2.2.1 on 2019-06-15 09:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('adm1', '0011_auto_20190615_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
