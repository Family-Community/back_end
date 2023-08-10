# Generated by Django 4.2.4 on 2023-08-10 06:38

import contents.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('content', models.CharField(blank=True, max_length=80, null=True)),
                ('photo', models.ImageField(max_length=150, upload_to=contents.models.user_photo_path)),
                ('date', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.member')),
            ],
        ),
        migrations.CreateModel(
            name='CreateContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('content', models.CharField(blank=True, max_length=80, null=True)),
                ('photo', models.ImageField(max_length=150, upload_to=contents.models.user_photo_path)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.member')),
            ],
        ),
    ]
