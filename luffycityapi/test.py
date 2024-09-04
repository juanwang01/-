# 用于测试
from django.core.cache import cache

# 尝试设置一个键值对
cache.set('my_key', 'my_value', timeout=60)

# 尝试获取刚刚设置的值
value = cache.get('my_key')
print(value)
