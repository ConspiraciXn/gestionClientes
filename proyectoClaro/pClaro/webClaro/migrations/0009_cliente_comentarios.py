# Generated by Django 3.2.5 on 2021-07-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webClaro', '0008_alter_cliente_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='comentarios',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
