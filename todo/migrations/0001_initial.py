# Generated by Django 5.1.3 on 2024-12-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(verbose_name='Data de Entrega')),
                ('finished_at', models.DateField(null=True)),
            ],
            options={
                'ordering': ['deadline'],
            },
        ),
    ]