# Generated by Django 4.2.1 on 2023-08-24 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_alter_messages_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="messages",
            options={"managed": True},
        ),
    ]
