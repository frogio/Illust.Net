# Generated by Django 4.1.1 on 2022-10-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("IllustNet", "0005_alter_illustpost_brief_comment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="illustpost",
            name="title",
            field=models.CharField(default="", max_length=300, null=True),
        ),
    ]
