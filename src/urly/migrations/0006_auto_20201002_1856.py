# Generated by Django 3.1.2 on 2020-10-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urly', '0005_auto_20201002_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcode',
            name='lastRedirect',
            field=models.DateTimeField(null=True),
        ),
    ]