# Generated by Django 4.2.11 on 2024-04-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brands | Shop Details'},
        ),
        migrations.AddField(
            model_name='brand',
            name='title',
            field=models.TextField(default='', help_text='Enter Brands | Shop Name ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brandmenu',
            name='item_name',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]