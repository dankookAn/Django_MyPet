# Generated by Django 4.2.1 on 2023-05-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0004_remove_feed_profile_image_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='profile_image',
            field=models.TextField(default='https://blog.kakaocdn.net/dn/bj4oa7/btqLJWFLMgd/wu4GV8PKbXdICuyW0me0zk/img.jpg'),
        ),
    ]