# Generated by Django 3.2.5 on 2021-07-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webClaro', '0007_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]