# Generated by Django 5.0.3 on 2024-06-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0012_alter_bookmodel_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='ISBN',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
