# Generated by Django 2.0.5 on 2018-07-14 04:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0005_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='items',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 14, 4, 28, 17, 427880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addcart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addCart', to='mainApp.Items'),
        ),
        migrations.AddField(
            model_name='addcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
