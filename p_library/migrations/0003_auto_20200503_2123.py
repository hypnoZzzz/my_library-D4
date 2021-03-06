# Generated by Django 2.2.6 on 2020-05-03 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Author'),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='имя')),
                ('books', models.ManyToManyField(to='p_library.Book', verbose_name='Книги')),
            ],
            options={
                'verbose_name': 'друг',
                'verbose_name_plural': 'друзья',
            },
        ),
        migrations.CreateModel(
            name='BookReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion', models.NullBooleanField(default=None, verbose_name='Чтение завершено')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookreading_book', to='p_library.Book', verbose_name='Книга')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookreading_friend', to='p_library.Friend', verbose_name='Читатель')),
            ],
        ),
    ]
