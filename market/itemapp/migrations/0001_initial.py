# Generated by Django 4.1.7 on 2023-02-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted?')),
                ('name', models.CharField(max_length=150, verbose_name='item name')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
