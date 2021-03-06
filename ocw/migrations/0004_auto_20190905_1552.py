# Generated by Django 2.1.7 on 2019-09-05 15:52

from django.db import migrations, models
import ocw.models


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0003_instance_notified'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='vault_namespace',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='instance',
            name='active',
            field=models.BooleanField(default=False, help_text='True if the last sync found this instance on CSP'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='state',
            field=models.CharField(choices=[('UNK', 'unkown'), ('ACTIVE', 'active'), ('DELETING', 'deleting'), ('DELETED', 'deleted')], default=ocw.models.StateChoice('unkown'), help_text='Local computed state of that Instance', max_length=8),
        ),
    ]
