dic = {}

def creat() :
    name = input("이름을 입력 해 주세요: ")
    age = input("나이를 입력 해 주세요: ")
    dic[name]=age

def read():
    print("------- 나이데이터베이스 -------")
    for name in dic:
        print(name,' : ',dic[name])
    print("-------------------------------")

def update():
    read()
    name = input("나이를 수정할 이름을 적어주세요: ")
    age = input("수정할 나이를 적어주세요: ")
    dic[name] = age

def delete():
    read()
    name = input("삭제할 사용자 이름을 입력해주세요: ")
    del dic[name]

print("나이 데이터베이스에 오신 걸 환영합니다.")

while True:
    menu = input("어떤 작업을 수행하시겠습니까? 1)생성하기 2)목록보기 3)수정하기 4)삭제하기 5)프로그램 끝내기 : ")
    if menu=="1":
        creat()
    elif menu=="2":
        read()
    elif menu=="3":
        update()
    elif menu=="4":
        delete()
    elif menu=="5":
        break