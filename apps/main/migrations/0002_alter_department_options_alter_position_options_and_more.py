# Generated by Django 5.1 on 2024-08-08 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'подразделение', 'verbose_name_plural': 'подразделении'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'должность', 'verbose_name_plural': 'должности'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'сотрудник', 'verbose_name_plural': 'сотрудники'},
        ),
    ]
