# Generated by Django 2.0.5 on 2018-07-14 06:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_auto_20180714_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addCart', to='mainApp.Items', unique=True),
        ),
        migrations.AlterField(
            model_name='addcart',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 14, 6, 28, 14, 87671, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 14, 6, 28, 14, 87671, tzinfo=utc)),
        ),
    ]
