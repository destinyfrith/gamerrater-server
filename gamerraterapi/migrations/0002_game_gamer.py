# Generated by Django 4.0.4 on 2022-05-12 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamerraterapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamerraterapi.gamer'),
        ),
    ]