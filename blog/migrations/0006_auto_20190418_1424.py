# Generated by Django 2.2 on 2019-04-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190418_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtype',
            name='blog_type',
            field=models.CharField(max_length=30, verbose_name='分类'),
        ),
    ]
