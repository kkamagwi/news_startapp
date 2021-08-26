# Generated by Django 3.2.5 on 2021-07-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=63)),
                ('phone_number', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('tag', models.ManyToManyField(related_name='tag', to='products.Tag')),
            ],
        ),
    ]
