# Generated by Django 2.2.10 on 2020-09-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0003_auto_20200912_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]