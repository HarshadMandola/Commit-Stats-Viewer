# Generated by Django 5.1.6 on 2025-02-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harrychart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dates', models.DateField(auto_now_add=True)),
                ('author_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('project_name', models.CharField(max_length=100)),
                ('hash_commit', models.CharField(max_length=50)),
                ('merge', models.BooleanField(verbose_name='merger status')),
                ('added_lines', models.IntegerField()),
                ('deleted_lines', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
