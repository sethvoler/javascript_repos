import requests as rs

# 执行API调用并存储响应
base = 'https://api.github.com/search/repositories'
query = '?q=language:javascript&sort=stars'
url = base + query
r = rs.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys())


