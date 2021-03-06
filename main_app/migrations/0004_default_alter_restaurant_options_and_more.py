# Generated by Django 4.0.5 on 2022-06-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_miles_options_remove_restaurant_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('img', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['restaurant']},
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='name',
            new_name='restaurant',
        ),
        migrations.RemoveField(
            model_name='miles',
            name='margarita',
        ),
        migrations.RemoveField(
            model_name='miles',
            name='price',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='img',
            field=models.CharField(default='Restaurant test', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='margarita',
            field=models.CharField(default='Margarita Test', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
