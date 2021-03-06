# Generated by Django 2.1.3 on 2018-12-17 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0013_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='username',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='question',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.Product'),
        ),
    ]
