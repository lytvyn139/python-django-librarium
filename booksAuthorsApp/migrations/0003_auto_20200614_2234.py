# Generated by Django 3.0.7 on 2020-06-14 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthorsApp', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='bookz', to='booksAuthorsApp.Author'),
        ),
    ]
