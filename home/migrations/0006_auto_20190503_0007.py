# Generated by Django 2.1.7 on 2019-05-03 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190502_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='menu_kakaoID',
            field=models.TextField(default='카카오 ID abc'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='menu_phonenumber',
            field=models.TextField(default='(213)386-6060'),
        ),
    ]