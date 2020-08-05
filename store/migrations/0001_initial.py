# Generated by Django 3.0.8 on 2020-07-26 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default='', max_length=500)),
                ('qty', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
            ],
        ),
    ]
