# Generated by Django 3.0.6 on 2020-08-12 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200811_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.CharField(choices=[('A', 'Actived'), ('D', 'Deleted')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('P', 'in-progress'), ('P', 'paused'), ('F', 'finished')], default='P', max_length=1),
        ),
    ]