# Generated by Django 3.1.2 on 2020-10-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urly', '0007_shortcode_redirectcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcode',
            name='redirectCount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]