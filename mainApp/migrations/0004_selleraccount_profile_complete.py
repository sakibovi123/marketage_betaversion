# Generated by Django 3.2.6 on 2021-09-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20210912_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleraccount',
            name='profile_complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
