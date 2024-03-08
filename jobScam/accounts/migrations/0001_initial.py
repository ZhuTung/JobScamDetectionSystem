# Generated by Django 4.2.4 on 2023-08-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.BigIntegerField(default=0)),
                ('username', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
