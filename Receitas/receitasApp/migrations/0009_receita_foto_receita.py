# Generated by Django 3.1.7 on 2021-03-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitasApp', '0008_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
