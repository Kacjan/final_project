# Generated by Django 4.2.6 on 2023-10-24 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0005_remove_courierday_courier_id_courierday_user_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
