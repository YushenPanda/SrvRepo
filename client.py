import requests
import json

# 服务器URL
url = "http://1.95.88.200:5000/compute"

# 要发送的数学表达式
expression = "1 + 4 * (1 - 2)"

# 创建请求数据
data = {
    "expression": expression
}

# 将数据转换为JSON格式
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

# 处理响应
if response.status_code == 200:
    result = response.json().get('result')
    print(f"The result of the expression '{expression}' is: {result}")
else:
    error_message = response.json().get('error')
    print(f"Error: {error_message}")
