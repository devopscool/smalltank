# Generated by Django 2.2 on 2020-04-22 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the entry's URL.", max_length=255, unique_for_date='publication_date', verbose_name='slug')),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')], db_index=True, default=0, verbose_name='status')),
                ('publication_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='publication date')),
            ],
            options={
                'ordering': ['-publication_date'],
                'abstract': False,
            },
        ),
    ]
