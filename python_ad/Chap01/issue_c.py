from bs4 import BeautifulSoup
import requests
from datetime import datetime

print(datetime.today().strftime("%Y년 %m월 %d일자 naver 실시간 기사\n"))

url = 'http://www.naver.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

results = soup.findAll('a','issue')

cnt = 1
f = open("issueresult.txt" , "w")

for result in results:
    data = str(cnt) + ". "+result.get_text() + "\n\n"
    print(data)
    f.write(data)
    cnt += 1

f.close()