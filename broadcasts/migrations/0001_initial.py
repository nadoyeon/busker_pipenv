# Generated by Django 3.2.5 on 2021-08-10 09:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('users', '0004_alter_user_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=80)),
                ('image', models.ImageField(blank=True, null=True, upload_to='genre_images')),
            ],
            options={
                'verbose_name': 'Genre',
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='PictureQuality',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Picture Quality',
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.timestampedmodel')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='broadcast_images/no_image.png', null=True, upload_to='broadcast_images')),
                ('on_air', models.BooleanField(default=False)),
                ('country', django_countries.fields.CountryField(default='South Korea', max_length=2)),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='broadcasts', serialize=False, to='users.user')),
                ('genres', models.ManyToManyField(blank=True, to='broadcasts.Genre')),
                ('picture_quality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='broadcasts.picturequality')),
            ],
            bases=('core.timestampedmodel',),
        ),
    ]
