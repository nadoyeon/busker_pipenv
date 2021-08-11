# Generated by Django 3.2.5 on 2021-08-09 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studios', '0004_auto_20210809_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='host',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studio',
            name='timestampedmodel_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.timestampedmodel'),
        ),
    ]
