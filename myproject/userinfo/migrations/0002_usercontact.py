# Generated by Django 3.2.5 on 2021-07-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('phonenumber', models.IntegerField()),
                ('question', models.TextField()),
            ],
        ),
    ]
