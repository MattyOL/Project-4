# Generated by Django 3.2.18 on 2023-05-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='recipe',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='method',
            field=models.TextField(blank=True),
        ),
    ]