# Generated by Django 3.2.6 on 2021-08-31 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0003_auto_20210831_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='welcome_msg',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
