# Generated by Django 3.0 on 2020-07-08 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(blank=True, max_length=100)),
                ('urunad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proje.Urun')),
            ],
        ),
    ]
