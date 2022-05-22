import requests

url = "https://www.naver.com/"
response = requests.get(url)

print(response)
print(response.text)

#print(result.url)

#print(result.content)

#print(result.encoding)

#print(result.headers)

#print(result.ok)

#print(result.status_code)