# Generated by Django 3.0.6 on 2020-08-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fieldName', models.FileField(upload_to='')),
            ],
        ),
    ]
