### dictionary로 분류하기
# total_dictionary = {}

# while True:
#     question = input("질문을 입력해주세요 : ")
#     if question == "q":
#         print("종료합니다.")
#         break
#     else :
#         total_dictionary[question] = ""

# for i in total_dictionary :
#     print(i)
#     answer = input("답변을 입력해주세요 : ")
#     total_dictionary[i] = answer

# print(total_dictionary)


### list로 분류
total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        print("종료합니다.")
        break
    else :
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list :
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer

print(total_list)