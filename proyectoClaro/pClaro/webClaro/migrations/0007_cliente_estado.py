# Generated by Django 3.2.5 on 2021-07-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webClaro', '0006_cliente_serviciotecnologia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
