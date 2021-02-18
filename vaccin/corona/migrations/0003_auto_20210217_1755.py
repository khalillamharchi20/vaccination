# Generated by Django 3.1.5 on 2021-02-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0002_individue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='sujet',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=5000),
        ),
    ]