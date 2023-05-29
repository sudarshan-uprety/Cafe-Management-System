# Generated by Django 4.2.1 on 2023-05-29 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_beakerycategory_drinkcategory_hukkacategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beakery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images/drinks')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.beakerycategory')),
            ],
        ),
    ]
