# Generated by Django 4.1.7 on 2023-03-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_alter_post_body_alter_post_title_departament_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='img',
            field=models.ImageField(default=76, upload_to='media/photo_doc'),
            preserve_default=False,
        ),
    ]