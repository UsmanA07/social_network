# Generated by Django 5.1.1 on 2024-09-30 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_likes_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
