# Generated by Django 4.2.4 on 2023-08-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_alter_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, height_field='100', null=True, upload_to='profile', width_field='100'),
        ),
    ]
