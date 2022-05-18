from django.test import TestCase

# Create your tests here.
import json

# 序列化将数据对象转换为一个标准格式字符串, 比如json字符串
data = {'name': "rain", 'age': 22, "is_married": False}
print(repr(json.dumps(data)))  # '{"name": "rain", "age": 22, "is_married": false}'

stus = ({'name': 'rain'}, {'name': 'admin'})
print(repr(json.dumps(stus)))  # '[{"name": "rain"}, {"name": "admin"}]'

# 反序列化
json_data = json.dumps(data)
data = json.loads(json_data)
print(data, type(data))
