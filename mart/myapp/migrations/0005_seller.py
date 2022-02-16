# Generated by Django 3.2.9 on 2022-01-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_addressee_raccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cSex', models.CharField(default='M', max_length=20)),
                ('cBirthday', models.DateField()),
                ('cEmail', models.EmailField(default='', max_length=50, null=True)),
                ('cPhone', models.CharField(default='', max_length=50, null=True)),
                ('cAddr', models.CharField(default='', max_length=100, null=True)),
                ('cAccount', models.CharField(default='', max_length=100, null=True)),
                ('cPswd', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
    ]