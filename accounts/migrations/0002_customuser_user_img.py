# Generated by Django 2.1.4 on 2019-12-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_img',
            field=models.FileField(blank=True, null=True, upload_to='static/images/profiles'),
        ),
    ]