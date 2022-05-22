import requests
# beautifulSoup을 import합니다.
from bs4 import BeautifulSoup
from datetime import datetime

print(datetime.today().strftime("%Y년 %m월 %d일자 naver 실시간 기사\n"))

url = 'https://www.naver.com/'
response = requests.get(url)

# BeautifulSoup 객체를 만듭니다.
# html 문자열에 대해서 parsing 하겠다.
soup = BeautifulSoup(response.text,'html.parser')

    # # 제일 위에있는 title 태그로 감싸진 부분
    # print(soup.title)
    # # title 태그 안에 있는 친구
    # print(soup.title.string)
    # print(soup.p)
    # print(soup.span)
    # print(soup.a)
    # # a 태그로 감싸진 모든 부분을 배열형태로 알려줌
    # print(soup.findAll('a'))

results = soup.findAll('a','issue')
# result에는 하나의 a태그가 들어가고, 그 태그의 text만 가져올 수 있는 get_text 메소드를 통해 원하는 정보만 출력합니다.
cnt = 1
for result in results:
    print(str(cnt) + ". " + result.get_text() + "\n")
    cnt += 1