# Generated by Django 3.2 on 2022-06-18 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookListLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('genre', models.TextField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'book_list_log',
            },
        ),
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('genre', models.TextField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'book_list',
            },
        ),
    ]