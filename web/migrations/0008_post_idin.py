# Generated by Django 4.1.3 on 2022-12-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_comment_post_connected'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='idin',
            field=models.IntegerField(default=0),
        ),
    ]
