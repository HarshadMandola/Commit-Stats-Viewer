# Generated by Django 5.1.6 on 2025-02-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issues',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issues',
            name='issue_id',
            field=models.CharField(default='0000', max_length=50),
        ),
        migrations.AlterField(
            model_name='issues',
            name='issue_key',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
