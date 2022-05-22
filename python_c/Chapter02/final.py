import random
import time

lunch = ["꿔바로우","떡볶이","삼겹살","포케"]

while True : 
    item = input("음식을 추가 해주세요 : ")
    if(item != "q") :
        lunch.append(item)
    else:
        break

print(lunch)

set_lunch = set(lunch)

while True :
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if(item != "q") :
        set_lunch = set_lunch - set([item])
    else :
        break

print(set_lunch, "중에서 선택합니다.")

for x in range(5) :
    print(5-x)
    time.sleep(1)

print(random.choice(list(set_lunch)))