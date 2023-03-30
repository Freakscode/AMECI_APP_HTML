# Generated by Django 4.1.7 on 2023-03-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicezk', '0002_deviceconnection_zk_alter_deviceconnection_conn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceconnection',
            name='zk',
        ),
        migrations.AddField(
            model_name='deviceconnection',
            name='device_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deviceconnection',
            name='firmware_version',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deviceconnection',
            name='serial_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='deviceconnection',
            name='conn',
            field=models.BooleanField(default=True),
        ),
    ]