# import random

# lunch = random.choice(["커피","케이크","까눌레"])
# dinner = random.choice(["시오빵","와플","휘낭시에"])

# print(lunch)

#------------------------

# information = {"고향":"서울","취미":"게임","좋아하는 음식":"초밥"}
# print(information)
# print(information.get("취미"))

# info2 = {"특기":"피아노","사는 곳":"서울"}
# print(info2.get("특기"))
# print(info2.get("사는 곳"))

#------------------------

information = {"고향":"서울","취미":"게임","좋아하는 음식":"초밥"}
foods = ["커피","케이크","까눌레"]

print(information.get("취미"))
information["특기"] = "금방 잠들기"
information["사는 곳"] = "서울"
del information["좋아하는 음식"]
print(information)
print(len(information))
information.clear()
print(information)

print(foods[2]) #음수 넣으면 뒤에서부터
foods.append("휘낭시에")
print(foods)
del foods[3]
print(foods)