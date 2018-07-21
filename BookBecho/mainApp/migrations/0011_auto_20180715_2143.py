# Generated by Django 2.0.5 on 2018-07-15 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20180715_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcart',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 15, 16, 13, 53, 960765, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 15, 16, 13, 53, 960765, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 15, 16, 13, 53, 960765, tzinfo=utc)),
        ),
    ]