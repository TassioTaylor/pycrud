# Generated by Django 2.2.5 on 2019-09-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.TextField()),
                ('fone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
