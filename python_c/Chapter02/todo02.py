""" 끝까지 반복하기

for x in range(30):
    print(x)

foods = ["커피","케이크","까눌레"]

for x in foods:
    print(x)

information = {"고향":"서울","취미":"게임","좋아하는 음식":"초밥"}

for x, y in information.items():
    print(x)
    print(y)

"""
""" 집합

menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 - menu2
print(menu3)

"""
""" 만약에
import random
food = random.choice(["커피","케이크","까눌레"])
if(food == "커피") :
    print(food+" 사이즈업 해주세요")
else :
    print(food+" 그냥 주세요")
print("종료")
"""