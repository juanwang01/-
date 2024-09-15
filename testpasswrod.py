import os
import django

# 设置 Django 项目的设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffycityapi/luffycityapi/settings/dev.py')
django.setup()

# 现在可以导入和使用 Django 模型了
from django.contrib.auth.hashers import make_password

password = '123'
hashed_password = make_password(password)
print(hashed_password)
