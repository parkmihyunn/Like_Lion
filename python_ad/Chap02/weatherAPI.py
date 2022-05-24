import requests
import json

apikey = ""
city = "Seoul"
lang = "kr"
unit = "metric"
# f-string은 문자열 사이에 변수를 포맷팅
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={unit}"

result = requests.get(api)
# json 타입으로 변환
data = json.loads(result.text)

#print("json :", data["weather"])  json형태로 변환된거니까 배열로 관리 가능함
# print("str :", result.text["weather"])  오류!

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 ",data["main"]["feels_like"],"일 거에요.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ", data["wind"]["deg"],"입니다.")
print("풍속은 ", data["wind"]["speed"],"입니다.")