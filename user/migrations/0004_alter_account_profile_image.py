# Generated by Django 4.2 on 2023-06-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_account_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='images/profile'),
        ),
    ]
