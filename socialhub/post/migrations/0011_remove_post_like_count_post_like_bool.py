# Generated by Django 5.1.1 on 2024-10-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_like_post_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.AddField(
            model_name='post',
            name='like_bool',
            field=models.BooleanField(default=False),
        ),
    ]
