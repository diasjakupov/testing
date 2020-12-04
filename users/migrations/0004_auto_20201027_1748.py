# Generated by Django 3.0.8 on 2020-10-27 11:48

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.DefineUserPathImages),
        ),
    ]
