# Generated by Django 5.2 on 2025-04-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
