# Generated by Django 3.0.1 on 2020-04-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200408_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='scantask',
            name='cookies',
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='scantask',
            name='target',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='scantask',
            name='target_type',
            field=models.CharField(default='link', max_length=30),
        ),
    ]