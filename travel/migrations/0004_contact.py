# Generated by Django 3.0.6 on 2020-05-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20200528_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField()),
            ],
        ),
    ]
