import json

# Python数据 → JSON字符串
python_data = {
    "name": "张三",
    "age": 25,
    "hobbies": ["读书", "运动"]
}

# 序列化：Python对象 → JSON字符串
json_str = json.dumps(python_data, ensure_ascii=False)
print("JSON字符串:")
print(json_str)

# 反序列化：JSON字符串 → Python对象
python_obj = json.loads(json_str)
print("\nPython对象:")
print(python_obj)