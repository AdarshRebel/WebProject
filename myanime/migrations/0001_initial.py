# Generated by Django 3.0.2 on 2022-07-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newanime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detials', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
