while True:
    a = int(input("몇단을 보실 예정인가요?: "))
    if(a<1 or a>9):
        print("구구단의 범위를 벗어났습니다.")
    else:
        for i in range(1,10):
            print(a," X ",i," = ",a*(i), end='\n')
        break
