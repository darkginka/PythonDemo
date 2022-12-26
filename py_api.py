import requests

# response = requests.get("https://official-joke-api.appspot.com/random_joke")
# print(response.json())
payload = dict(key1='value1', key2='value2')
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())