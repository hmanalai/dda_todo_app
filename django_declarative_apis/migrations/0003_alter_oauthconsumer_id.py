# Generated by Django 3.2.3 on 2021-05-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_declarative_apis', '0002_add_consumer_type_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauthconsumer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
