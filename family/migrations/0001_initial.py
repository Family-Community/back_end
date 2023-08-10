# Generated by Django 4.2.4 on 2023-08-10 06:09

from django.db import migrations, models
import django.db.models.deletion
import family.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=10)),
                ('family_code', models.CharField(default=family.models.generate_hash, editable=False, max_length=64)),
                ('color', models.CharField(max_length=7)),
                ('entry_number', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='family.group')),
            ],
        ),
    ]
