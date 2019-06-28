# Generated by Django 2.2 on 2019-06-28 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190524_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
