# Generated by Django 3.2.5 on 2021-07-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webClaro', '0004_alter_imagenperfil_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='vendedor',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
