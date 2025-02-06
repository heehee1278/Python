userid=input("아이디는?")
result1="콘텐츠 이용이 가능합니다"
result2="콘텐츠 이용할 수 없습니다"
if userid == "admin" :
    print(result1)

else:
    level=int(input("회원 레벨은(1~9)"))

    if level >=1 and level <=3:
        print(result1)

    else:
        print(result2)



