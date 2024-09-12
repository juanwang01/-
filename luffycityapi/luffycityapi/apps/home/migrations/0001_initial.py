# Generated by Django 4.2.15 on 2024-09-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='名称/标题')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('orders', models.IntegerField(default=0, verbose_name='序号')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('link', models.CharField(max_length=255, verbose_name='导航连接')),
                ('is_http', models.BooleanField(default=False, verbose_name='是否站外连接地址')),
                ('position', models.SmallIntegerField(choices=[(0, '顶部导航'), (1, '脚部导航')], default=0, verbose_name='导航位置')),
            ],
            options={
                'verbose_name': '导航菜单',
                'verbose_name_plural': '导航菜单',
                'db_table': 'fg_nav',
            },
        ),
    ]